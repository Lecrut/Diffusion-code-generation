import cairosvg

def generate_svg():
    width = 100
    height = 100
    rect_x = 10
    rect_y = 10
    rect_width = 50
    rect_height = 50
    fill_color = "green"
    
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers")
    if not (isinstance(rect_x, int) and isinstance(rect_y, int)):
        raise ValueError("Rectangle x and y coordinates must be integers")
    if not (isinstance(rect_width, int) and isinstance(rect_height, int)):
        raise ValueError("Rectangle width and height must be integers")
    if not isinstance(fill_color, str):
        raise ValueError("Fill color must be a string")
    
    svg_content = f"""
    <svg width="{width}" height="{height}">
        <rect x="{rect_x}" y="{rect_y}" width="{rect_width}" height="{rect_height}" fill="{fill_color}"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())