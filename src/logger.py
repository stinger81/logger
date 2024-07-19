# /bin/python3
# ##########################################################################
#
#   Copyright (C) 2022-2024 Michael Dompke (https://github.com/stinger81)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   Michael Dompke (https://github.com/stinger81)
#   michael@dompke.dev
#
# ##########################################################################
from typing import List, Dict, Any, Union
import datetime


class logger:
    def __init__(self,
                 files: Union[str, List[str]] = None,
                 debug: bool = False,
                 console: bool = True
                 ):
        self.files = files
        if files is None:
            self.files = []
        elif isinstance(files, str):
            self.files = [files]
        self.debug = debug
        self.console = console

    def log(self, message: Union[str, list, dict], level: str = 'INFO', delimiter:str=""):
        if delimiter != "":
            self._log_delimiter(message, delimiter, level)
        elif isinstance(message, str):
            if "\n" in message:
                self._log_delimiter(message, delimiter = "\n", level = level)
            else:
                self._log_str(message, level)
        elif isinstance(message, list):
            self._log_list(message, level)
        elif isinstance(message, dict):
            self._log_dict(message, level)

    def log_info(self, message: Union[str, list, dict], delimiter=""):
        self.log(message, 'INFO', delimiter)

    def log_warning(self, message: Union[str, list, dict], delimiter=""):
        self.log(message, 'WARNING', delimiter)

    def log_error(self, message: Union[str, list, dict], delimiter=""):
        self.log(message, 'ERROR', delimiter)

    def log_critical(self, message: Union[str, list, dict], delimiter=""):
        self.log(message, 'CRITICAL', delimiter)

    def dlog(self, message: Union[str, list, dict], level: str = 'DEBUG', delimiter=""):
        if self.debug:
            self.log(message, level, delimiter)

    def dlog_info(self, message: Union[str, list, dict], delimiter=""):
        self.dlog(message, 'DEBUG INFO', delimiter)

    def dlog_warning(self, message: Union[str, list, dict], delimiter=""):
        self.dlog(message, 'DEBUG WARNING', delimiter)

    def dlog_error(self, message: Union[str, list, dict], delimiter=""):
        self.dlog(message, 'DEBUG ERROR', delimiter)

    def dlog_critical(self, message: Union[str, list, dict], delimiter=""):
        self.dlog(message, 'DEBUG CRITICAL', delimiter)

    def _log_dict(self, message: dict, level: str = 'INFO'):
        pass

    def _log_list(self, message: list, level: str = 'INFO'):
        pass

    def _log_str(self, message: str, level: str = 'INFO'):
        pass

    def _log_delimiter(self, message: str,  delimiter:str, level: str= 'INFO'):
        pass


    def _build_msg_header(self, level: str):
        timestamp = datetime.datetime.now().isoformat()
        return self._build_msg_header_console(level, timestamp), self._build_msg_header_file(level, timestamp)

    def _build_msg_header_console(self, level: str, timestamp: str):
        return f"{timestamp} [{level}]:"

    def _build_msg_header_file(self, level: str, timestamp: str):
        return f"{timestamp} [{level}]:"
