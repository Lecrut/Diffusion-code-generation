import io
import svgwrite

class SVGGenerator:
    RECT_ID = 'box1'
    RECT_POSITION = (50, 50)
    RECT_SIZE = (100, 100)
    RECT_FILL_COLOR = '#FF0000'

    @staticmethod
    def generate_svg():
        dwg = svgwrite.Drawing()
        rect = dwg.rect(insert=SVGGenerator.RECT_POSITION, size=SVGGenerator.RECT_SIZE, fill=SVGGenerator.RECT_FILL_COLOR, id=SVGGenerator.RECT_ID)
        dwg.add(rect)
        return io.StringIO(dwg.tostring()).getvalue()

if __name__ == '__main__':
    svg_content = SVGGenerator.generate_svg()
    print(svg_content)