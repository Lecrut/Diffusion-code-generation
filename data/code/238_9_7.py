import cairosvg

def generate_svg():
    dimensions = {
        'width': 100,
        'height': 100
    }
    rect_properties = {
        'x': 10,
        'y': 10,
        'width': 50,
        'height': 50,
        'fill': 'green'
    }

    svg_content = f"""
    <svg width="{dimensions['width']}" height="{dimensions['height']}">
        <rect x="{rect_properties['x']}" y="{rect_properties['y']}" width="{rect_properties['width']}" height="{rect_properties['height']}" fill="{rect_properties['fill']}"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())