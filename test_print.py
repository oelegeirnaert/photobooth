import cups
from PIL import Image
from tempfile import mktemp
from time import sleep
import base64
import sys

# Set up CUPS
conn = cups.Connection()
printers = conn.getPrinters()
print(printers)
#sys.exit()
printer_name = printers.keys()
print(printer_name)
cups.setUser('pi')

# Image (code taken from boothcam.py)
myFile = '/home/pi/photobooth/2019-02-19/photobooth00005.jpg'


# Send the picture to the printer
print_id = conn.printFile("photobooth_printer", myFile, "photobooth_printer", {})
# Wait until the job finishes
while conn.getJobs().get(print_id, None):
    sleep(1)
    
print(print_id)

