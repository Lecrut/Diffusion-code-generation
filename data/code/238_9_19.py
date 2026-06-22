import cairosvg

class SVGGenerator:
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
        <svg width="{SVGGenerator.WIDTH}" height="{SVGGenerator.HEIGHT}">
            <rect x="{SVGGenerator.RECT_X}" y="{SVGGenerator.RECT_Y}" width="{SVGGenerator.RECT_WIDTH}" height="{SVGGenerator.RECT_HEIGHT}" fill="{SVGGenerator.FILL_COLOR}"/>
        </svg>
        """
        return svg_content

if __name__ == '__main__':
    print(SVGGenerator.generate_svg())