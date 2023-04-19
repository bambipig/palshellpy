import subprocess


def get_user_home_dir():
    return subprocess.getoutput('echo $HOME').strip()

