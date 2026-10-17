"""Собирает cv.pdf из cv.html.

python tools/build-pdf.py <chrome-headless-shell.exe>
"""
import os, subprocess, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pdf = os.path.join(SITE, 'cv.pdf')
subprocess.run([sys.argv[1], '--headless', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
                f'--print-to-pdf={pdf}', 'file:///' + os.path.join(SITE, 'cv.html').replace('\\', '/')],
               stderr=subprocess.DEVNULL, check=True)
print(pdf, round(os.path.getsize(pdf) / 1024), 'KB')
