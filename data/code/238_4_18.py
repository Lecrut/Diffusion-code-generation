import io
import svgwrite

def create_rectangle(id, insert, size, fill):
    return svgwrite.shapes.Rect(insert=insert, size=size, fill=fill, id=id)

def generate_svg():
    dwg = svgwrite.Drawing()
    rect = create_rectangle('box1', (50, 50), (100, 100), '#FF0000')
    dwg.add(rect)
    return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = generate_svg()
    print(svg_content)