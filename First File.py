import win32print
import win32ui

printer_name = "TaskPrinterWireless"  # replace with your printer's name
hprinter = win32print.OpenPrinter(printer_name)
job = win32print.StartDocPrinter(hprinter, 1, ("Test Job", None, "RAW"))
win32print.StartPagePrinter(hprinter)
win32print.WritePrinter(hprinter, b"Hello Dillon!\n\n\n\n")
win32print.EndPagePrinter(hprinter)
win32print.EndDocPrinter(hprinter)
win32print.ClosePrinter(hprinter)
