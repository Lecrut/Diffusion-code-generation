import io
import svgwrite

def generate_svg():
    drawing = svgwrite.Drawing()
    rectangle = drawing.rect(insert=(50, 50), size=(100, 100), fill='#FF0000')
    rectangle['id'] = 'box1'
    drawing.add(rectangle)
    return io.StringIO(drawing.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = generate_svg()
    print(svg_content)