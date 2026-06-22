import io
import svgwrite

class SVGGenerator:
    DEFAULT_RECT_ID = 'box1'
    DEFAULT_RECT_INSERT = (50, 50)
    DEFAULT_RECT_SIZE = (100, 100)
    DEFAULT_RECT_FILL = '#FF0000'

    @staticmethod
    def generate_svg(rect_id=None, insert=None, size=None, fill=None):
        rect_id = rect_id or SVGGenerator.DEFAULT_RECT_ID
        insert = insert or SVGGenerator.DEFAULT_RECT_INSERT
        size = size or SVGGenerator.DEFAULT_RECT_SIZE
        fill = fill or SVGGenerator.DEFAULT_RECT_FILL

        dwg = svgwrite.Drawing()
        rect = dwg.rect(insert=insert, size=size, fill=fill)
        rect['id'] = rect_id
        dwg.add(rect)
        return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = SVGGenerator.generate_svg()
    print(svg_content)