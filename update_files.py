import sys
import os

def update_files():
    fm_file = open('frontmatter.txt')
    fm_txt = fm_file.read()
    fm_file.close()
    files = os.listdir('cheatsheets')
    for filename in files:
        front = fm_txt
        path = os.path.join('cheatsheets/' + filename)
        cs_file = open(path, mode='rt+')
        cs_text = cs_file.read()
        cs_file.close()
        tags = 'cheat sheets, '
        if 'layout:' not in cs_text:
            parts = filename.split('_')
            title = ''
            for part in parts:
                if 'Cheat' in part:
                    break
                if len(title) > 0:
                    title += ' '
                title += part
            tags += title
            front = front.replace('{:pagetitle}', title)
            front = front.replace('{:tags}', tags)
            cs_text = front + '\n' + cs_text
            cs_file = open(path, mode='w')
            cs_file.write(cs_text)
            cs_file.close()
        

update_files()