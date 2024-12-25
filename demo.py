from us_visa.logger import logging 
from us_visa.exception import USvisaException
import sys
logging.info("i am learning the MLOPs")
try: 
    a=2/0 
except Exception as e: 
    raise USvisaException(e,sys)