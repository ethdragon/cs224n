from docx import Document
from docx.enum.text import WD_COLOR_INDEX

document = Document('test.docx')

for paragraph in document.paragraphs:
    for run in paragraph.runs:
        font = run.font
        if font.highlight_color == WD_COLOR_INDEX.YELLOW:
            print('%s %s %s' % (font.highlight_color, run.text, font.highlight_color))
        else:
            print(run.text)
    print('\n')
