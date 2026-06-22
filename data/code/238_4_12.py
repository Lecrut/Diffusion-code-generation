import io
import svgwrite

def create_svg_element():
    dwg = svgwrite.Drawing()
    rect = dwg.rect(insert=(50, 50), size=(100, 100), fill='#FF0000', id='box1')
    dwg.add(rect)
    return dwg.tostring()

if __name__ == '__main__':
    svg_content = create_svg_element()
    print(svg_content.decode('utf-8'))