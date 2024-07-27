from sys import version as PYTHON_VERSION
from time import localtime, time
from platform import system as ops
import os
from zipfile import ZipFile

AKLOGS_VERSION = "AkLogs v0.0.1 BETA"

global t1, t2
t1 = 0
t2 = 0

def define_log_name():
    zmienna = localtime[2] + "." + localtime[1] + "." + localtime[0] + "r-" +  localtime[3] + ":" + localtime[4] + ":" + localtime[5] + ".zip"
    return zmienna

def clear_screen():
    if ops == "Windows":
        os.system('cls')
    elif ops == "Linux":
        os.system('clear')

def zip_log(path, zip_file_name):
    with ZipFile(path, "w") as zipf:
        zipf.write(zip_file_name)

def add_to_log(log_file, var_to_add, insert_date=False, insert_type=None):
    if insert_date:
        data = f"[{localtime[2]}.{localtime[1]}.{localtime[0]}r][{localtime[3]}:{localtime[4]}:{localtime[5]}][{insert_type}] "
        print(data + var_to_add)
        log_file.append(data + var_to_add + "\n")
    else:
        print(var_to_add)
        log_file.append(var_to_add + "\n")

class HandleLog:
    def __init__(self, program_name, program_version, copyright="siema", log_name="logs/latest.log", define_log_name_f = define_log_name):
        self.log_name = log_name
        self.program_name = program_name
        self.program_version = program_version
        self.copyright = copyright
        self.zip_name = define_log_name()
    def start_making_log(self):
        t1 = time()
        with open(self.log_name, "w") as plik:
            plik.write("")
            add_to_log(log_file=plik, var_to_add=self.program_name + self.program_version)
            add_to_log(log_file=plik, var_to_add=self.copyright)
            add_to_log(log_file=plik, var_to_add=f"This file is using {AKLOGS_VERSION}")
            add_to_log(log_file=plik, var_to_add=f"Using Python {PYTHON_VERSION}")
    def append_log(self, log_type, var_to_add):
        with open(self.log_name, "w") as plik:
            add_to_log(log_file=plik, var_to_add=var_to_add, insert_date=True, insert_type=log_type)
    def end_log(self):
        t2 = time()
        with open(self.log_name, "w") as plik:
            add_to_log(log_file=plik, var_to_add=self.copyright)
            add_to_log(log_file=plik, var_to_add=f"Program działał przez {int(t2-t1)} sekund")
        if not os.path.exists("logs"):
            os.makedirs("logs")
        zip_log(f"logs/{self.zip_name}",self.log_name)