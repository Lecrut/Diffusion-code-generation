import svgwrite

def generate_svg():
    dwg = svgwrite.Drawing()
    rect = dwg.rect(insert=(50, 50), size=(100, 100), fill='#FF0000', id='box1')
    return dwg.tostring()

if __name__ == '__main__':
    print(generate_svg())