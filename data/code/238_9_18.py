import cairosvg

def generate_svg():
    svg_content = f"""
    <svg width="100" height="100">
        <rect x="10" y="10" width="50" height="50" fill="green"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())