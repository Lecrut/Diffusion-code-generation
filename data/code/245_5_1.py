import math
def compare_areas(shape1, shape2):
    area1 = 0
    area2 = 0
    if shape1['type'] == 'rectangle':
        length = shape1['length']
        width = shape1['width']
        area1 = length * width
    elif shape1['type'] == 'circle':
        radius = shape1['radius']
        area1 = math.pi * (radius ** 2)
    elif shape1['type'] == 'triangle':
        base = shape1['base']
        height = shape1['height']
        area1 = 0.5 * base * height
    else:
        return False
    if shape2['type'] == 'rectangle':
        length = shape2['length']
        width = shape2['width']
        area2 = length * width
    elif shape2['type'] == 'circle':
        radius = shape2['radius']
        area2 = math.pi * (radius ** 2)
    elif shape2['type'] == 'triangle':
        base = shape2['base']
        height = shape2['height']
        area2 = 0.5 * base * height
    else:
        return False
    return area1 == area2
if __name__ == '__main__':
    shape_a = {'type': 'rectangle', 'length': 4, 'width': 5}
    shape_b = {'type': 'rectangle', 'length': 10, 'width': 2}
    shape_c = {'type': 'circle', 'radius': 3}
    shape_d = {'type': 'circle', 'radius': 2}
    shape_e = {'type': 'triangle', 'base': 6, 'height': 4}
    shape_f = {'type': 'triangle', 'base': 8, 'height': 3}
    print(f"Areas of A ({shape_a['type']}: {shape_a['length']}x{shape_a['width']}) and B ({shape_b['type']}: {shape_b['length']}x{shape_b['width']}) are equal: {compare_areas(shape_a, shape_b)}")
    print(f"Areas of C ({shape_c['type']}: radius={shape_c['radius']}) and D ({shape_d['type']}: radius={shape_d['radius']}) are equal: {compare_areas(shape_c, shape_d)}")
    print(f"Areas of E ({shape_e['type']}: base={shape_e['base']}, height={shape_e['height']}) and F ({shape_f['type']}: base={shape_f['base']}, height={shape_f['height']}) are equal: {compare_areas(shape_e, shape_f)}")