import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno

    def str(self):
        return (f"Error occured in python script"f"[{self.file_name}]"
                f"in line number"f"[{self.lineno}]"f"with error message being :"f"[{self.error_message}]")
        

