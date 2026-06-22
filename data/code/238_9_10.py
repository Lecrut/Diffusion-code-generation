import cairosvg

class SVGGenerator:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.rect_x = 10
        self.rect_y = 10
        self.rect_width = 50
        self.rect_height = 50
        self.fill_color = "green"

    def generate_svg(self):
        svg_content = f"""
        <svg width="{self.width}" height="{self.height}">
            <rect x="{self.rect_x}" y="{self.rect_y}" width="{self.rect_width}" height="{self.rect_height}" fill="{self.fill_color}"/>
        </svg>
        """
        return svg_content

if __name__ == '__main__':
    generator = SVGGenerator()
    print(generator.generate_svg())