import cairosvg

def generate_svg():
    width = 100
    height = 100
    rect_x = 20
    rect_y = 20
    rect_width = 60
    rect_height = 60
    fill_color = "blue"
    
    svg_content = f"""
    <svg width="{width}" height="{height}">
        <rect x="{rect_x}" y="{rect_y}" width="{rect_width}" height="{rect_height}" fill="{fill_color}"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())