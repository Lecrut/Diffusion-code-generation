import io
import svgwrite

def generate_svg():
    RECT_ID = 'box1'
    RECT_POSITION = (50, 50)
    RECT_SIZE = (100, 100)
    RECT_FILL_COLOR = '#FF0000'

    dwg = svgwrite.Drawing()
    rect = dwg.rect(insert=RECT_POSITION, size=RECT_SIZE, fill=RECT_FILL_COLOR, id=RECT_ID)
    dwg.add(rect)
    return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = generate_svg()
    print(svg_content)