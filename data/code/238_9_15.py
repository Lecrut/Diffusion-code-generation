import cairosvg

class SvgGenerator:
    WIDTH = 100
    HEIGHT = 100
    RECT_X = 10
    RECT_Y = 10
    RECT_WIDTH = 50
    RECT_HEIGHT = 50
    FILL_COLOR = "green"

    @staticmethod
    def generate_svg():
        svg_content = f"""
        <svg width="{SvgGenerator.WIDTH}" height="{SvgGenerator.HEIGHT}">
            <rect x="{SvgGenerator.RECT_X}" y="{SvgGenerator.RECT_Y}" width="{SvgGenerator.RECT_WIDTH}" height="{SvgGenerator.RECT_HEIGHT}" fill="{SvgGenerator.FILL_COLOR}"/>
        </svg>
        """
        return svg_content

if __name__ == '__main__':
    print(SvgGenerator.generate_svg())