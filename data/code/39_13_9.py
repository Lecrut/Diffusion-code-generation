GEOMETRY_CONSTANTS = {
    'base_area': 12.5,
    'height': 6.0
}

def get_prism_volume(area, height):
    result = area * height
    return result

if __name__ == '__main__':
    b = GEOMETRY_CONSTANTS['base_area']
    h = GEOMETRY_CONSTANTS['height']
    v = get_prism_volume(b, h)
    print(v)