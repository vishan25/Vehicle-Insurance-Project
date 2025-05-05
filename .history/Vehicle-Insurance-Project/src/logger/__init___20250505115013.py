import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime


LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024
BACKU