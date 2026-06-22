import cairosvg

def generate_svg():
    width = 100
    height = 100
    rect_x = 10
    rect_y = 10
    rect_width = 50
    rect_height = 50
    fill_color = "green"

    svg_content = f"""
    <svg width="{width}" height="{height}">
        <rect x="{rect_x}" y="{rect_y}" width="{rect_width}" height="{rect_height}" fill="{fill_color}"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())