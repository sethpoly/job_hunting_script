# This script opens all the necessary
# websites/files for me to start a job-hunting session
import webbrowser, os

# List with job boards, spreadsheet with all jobs applied to, github, etc
websites = ['https://www.linkedin.com/jobs/',
            'https://docs.google.com/spreadsheets/d/1oTRHF8gxZEyyQdsbroqITl6YUymR6CuwkXp47j1cFsY/edit#gid=0',
            'https://github.com/sethpoly',
            ]
# Current resume
resume = r'"C:\Users\Seth\Desktop\Resume2021\SethPolyniakResume.pdf"'

# List with misc files to open
files = [resume]

# Opens all the sites in the list in new tabs
def open_sites():
    for site in websites:
        print(f'Opening site: {site}')
        webbrowser.open_new_tab(site)

# Open all files in list 
def open_files():
    for file in files:
        print(f'Opening file: {file}')
        os.startfile(file)


open_sites()
open_files()
