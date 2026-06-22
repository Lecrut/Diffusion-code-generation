import cairosvg

def generate_filled_square_svg():
    svg = f'<svg width="60" height="60"><rect x="10" y="10" width="50" height="50" fill="green"/></svg>'
    return svg

if __name__ == '__main__':
    print(generate_filled_square_svg())