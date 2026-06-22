import io
import svgwrite

class SVGGenerator:
    def __init__(self):
        self.dwg = svgwrite.Drawing()

    def add_rectangle(self, insert, size, fill, id):
        rect = self.dwg.rect(insert=insert, size=size, fill=fill)
        rect['id'] = id
        self.dwg.add(rect)

    def get_svg_string(self):
        return io.StringIO(self.dwg.tostring()).getvalue()

if __name__ == '__main__':
    generator = SVGGenerator()
    generator.add_rectangle((50, 50), (100, 100), '#FF0000', 'box1')
    svg_content = generator.get_svg_string()
    print(svg_content)