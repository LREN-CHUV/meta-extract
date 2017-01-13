import logging
from . import connection

########################################################################################################################
# SETTINGS
########################################################################################################################

ACQUISITION_STEP_NAME = 'acquisition'
VISIT_STEP_NAME = 'visit'


########################################################################################################################
# PUBLIC FUNCTION
########################################################################################################################

def visit(folder, provenance_id, previous_step_id=None, db_url=None):
    """
    Record all files from a folder into the database.
    The files are listed in the DB. If a file has been copied from previous step without any transformation, it will be
    detected and marked in the DB. The type of file will be detected and stored in the DB. If a files (e.g. a DICOM
    file) contains some meta-data, those will be stored in the DB.
    :param folder: folder path.
    :param provenance_id: provenance label.
    :param previous_step_id: (optional) previous processing step ID. If not defined, we assume this is the first
    processing step.
    :param db_url: (optional) Database URL. If not defined, it looks for an Airflow configuration file.
    :return: return processing step ID.
    """
    logging.info("Running visit function with the following parameters : "
                 "folder=%s, provenance_id=%s, step_id=%s, db_url=%s",
                 (folder, provenance_id, previous_step_id, db_url))

    db_conn = connection.Connection(db_url)

    if not previous_step_id:
        step_id = create_step(db_conn, ACQUISITION_STEP_NAME, provenance_id)
        record_files(db_conn, folder, provenance_id, step_id)
    else:
        step_id = create_step(db_conn, VISIT_STEP_NAME, provenance_id, previous_step_id)
        visit_results(db_conn, folder, provenance_id, step_id)

    return step_id


def create_provenance(dataset, matlab_version=None, spm_version=None, spm_revision=None, fn_called=None,
                      fn_version=None, others=None):
    """
    Create a provenance entity, store it in the database and get back a provenance ID.
    :param dataset: Name of the data set.
    :param matlab_version: (optional) Matlab version.
    :param spm_version: (optional) SPM version.
    :param spm_revision: (optional) SPM revision.
    :param fn_called: (optional) Function called.
    :param fn_version: (optional) Function version.
    :param others: (optional) Any other information can be set using this field.
    :return: Provenance ID.
    """
    provenance_id = None

    return provenance_id


########################################################################################################################
# PRIVATE FUNCTION
########################################################################################################################

def create_step(db_conn, ACQUISITION_STEP_NAME, provenance_id, previous_step_id=None):
    step_id = None
    return step_id


def record_files(db_conn, folder, provenance_id, step_id):
    pass


def visit_results(db_conn, folder, provenance_id, step_id):
    pass
