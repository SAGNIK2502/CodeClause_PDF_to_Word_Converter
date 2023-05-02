from pdf2docx import Converter
pdf='res.pdf'
docx='newres.docx'
cv= Converter(pdf)
cv.convert(docx)