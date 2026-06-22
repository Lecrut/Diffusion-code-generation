import io
import svgwrite

def create_rectangle():
    rect = svgwrite.shapes.Rect(insert=(50, 50), size=(100, 100), fill='#FF0000')
    rect['id'] = 'box1'
    return rect

def generate_svg(rect):
    dwg = svgwrite.Drawing()
    dwg.add(rect)
    return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    rectangle = create_rectangle()
    svg_content = generate_svg(rectangle)
    print(svg_content)