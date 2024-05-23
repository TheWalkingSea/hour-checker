import psutil
import time
import subprocess
import json
import datetime

CONFIG = None
with open("./config.json", "r") as f:
    CONFIG = json.load(f)

def is_process_running(process_name: str) -> bool:
    """
    Check if a process with the given name is running.
    """
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

def getRootPath(app_name: str) -> str:
    return app_name.split("/")[-1]

def updateTimestamp(dtime: int) -> None:
    with open("out", "r") as f:
        timestamp = int(f.readline())
    with open("out", "w") as f:
        f.write(str(timestamp + dtime))

def loop(app_name: str) -> bool:
    if (is_process_running(getRootPath(app_name))):
        updateTimestamp(CONFIG['checkInterval'])
        return True
    return False


def run_exe(app_name: str):
    subprocess.Popen(app_name, shell=True)

if __name__ == "__main__":
    run_exe(CONFIG['program'])
    flag = True
    while (flag):
        time.sleep(CONFIG['checkInterval'])
        flag = loop(CONFIG['program'])