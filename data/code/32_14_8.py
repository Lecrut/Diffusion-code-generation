AREA_UNITS = {
    'metric': 1,
    'imperial': 1,
    'default': 1
}

def compute_rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    width = 15
    height = 8
    current_unit = 'default'
    multiplier = AREA_UNITS[current_unit]
    area = compute_rectangle_area(width, height) * multiplier
    print(area)