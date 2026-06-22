import io
import svgwrite

# Constants for SVG dimensions and properties
SVG_WIDTH = 200
SVG_HEIGHT = 200
RECT_INSERT_X = 50
RECT_INSERT_Y = 50
RECT_SIZE_WIDTH = 100
RECT_SIZE_HEIGHT = 100
RECT_FILL_COLOR = '#FF0000'
RECT_ID = 'box1'

def generate_svg():
    dwg = svgwrite.Drawing(size=(SVG_WIDTH, SVG_HEIGHT))
    rect = dwg.rect(insert=(RECT_INSERT_X, RECT_INSERT_Y), size=(RECT_SIZE_WIDTH, RECT_SIZE_HEIGHT), fill=RECT_FILL_COLOR)
    rect['id'] = RECT_ID
    dwg.add(rect)
    return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = generate_svg()
    print(svg_content)