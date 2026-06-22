import cairosvg

def generate_green_square_svg():
    svg_content = f"""
    <svg width="50" height="50">
        <rect x="10" y="10" width="50" height="50" fill="green"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_green_square_svg())