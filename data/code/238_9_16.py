import cairosvg

SVG_WIDTH = 100
SVG_HEIGHT = 100
RECT_X = 10
RECT_Y = 10
RECT_WIDTH = 50
RECT_HEIGHT = 50
FILL_COLOR = "green"

def generate_svg():
    svg_content = f"""
    <svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
        <rect x="{RECT_X}" y="{RECT_Y}" width="{RECT_WIDTH}" height="{RECT_HEIGHT}" fill="{FILL_COLOR}"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())