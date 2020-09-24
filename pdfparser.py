import os
import PyPDF2 as p2


# Method which goes file by file in directory - Will call the file reader
#path of where resumes are located

path = "thisisatestpath/path"
directory = os.listdir(path)

for pdf in directory:

    pdfdir = path + "/" + pdf

    try:
        PDFfile = open(pdfdir, "rb")
        pdfRead = p2.PdfFileReader(PDFfile)
        x = pdfRead.getPage(0)
    
    except: 
        PDFfile.close()
        os.remove(pdfdir)
        continue

    print(pdfdir)
    if 'florida international university'  in x.extractText().lower() or 'fiu' in x.extractText().lower() : 
        print("it is")
    # if 'Honors College'.lower() in x.extractText().lower() : 
    #     print("it is")
    else : 
        PDFfile.close()
        os.remove(pdfdir)


    # if 'Florida International University' or 'FIU' in x.extractText() : 
    #     print("it is")

    # else : 
    #     PDFfile = close(pdfdir, "rb")
    #     os.remove(pdfdir)

