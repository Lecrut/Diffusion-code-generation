import cairosvg

def generate_svg():
    svg_content = """
    <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="50" height="50" fill="green"/>
    </svg>
    """
    return svg_content

if __name__ == '__main__':
    print(generate_svg())