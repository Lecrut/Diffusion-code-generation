import io
import svgwrite

def generate_svg():
    dwg = svgwrite.Drawing()
    rect = dwg.rect(insert=(50, 50), size=(100, 100), fill='#FF0000')
    rect['id'] = 'box1'
    dwg.add(rect)
    return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = generate_svg()
    print(svg_content)