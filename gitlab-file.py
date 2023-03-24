import gitlab
import sys
import os
import argparse

#Example
# sudo python3 gitlab-file.py --metrics_block test-env 
# test-env - folder in gitlab project


def check_folder(CONFIG_FOLDER):
        isExist = os.path.exists(CONFIG_FOLDER)
        if not isExist:
                os.makedirs(CONFIG_FOLDER)

##variables
GITLAB_URL = 'https://your.company.com'
API_TOKEN = 'you-app-gitlab-token'
BRANCH = 'your-main'
arg = argparse.ArgumentParser()
arg.add_argument('--metrics_block', dest='metrics_block', type=str, help='Add metrics block' )
arguments = arg.parse_args()
METRICS_BLOCK = arguments.metrics_block
FILE = 'your-file-in-repo.txt'
PROJECT_NAME = "your-group/your-project"
CONFIG_FOLDER = '/your/dest/folder' + METRICS_BLOCK + '/'
CONFIG_PATH = CONFIG_FOLDER  + FILE
GITLAB_FILE = METRICS_BLOCK + '/' + FILE
#End of variables
##
gl = gitlab.Gitlab(GITLAB_URL, private_token=API_TOKEN, ssl_verify=False)
check_folder(CONFIG_FOLDER)
project_name = PROJECT_NAME

project = gl.projects.get(project_name)
f = project.files.get(file_path=GITLAB_FILE, ref=BRANCH)
out_file = open(CONFIG_PATH, "wb")
result = f.decode()
out_file.write(result)
out_file.close()
