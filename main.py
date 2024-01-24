import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from heart_disease_pred.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

stage_name = "Data Ingestion"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)




stage_name = "Data Validation"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)


