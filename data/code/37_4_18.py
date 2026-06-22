def get_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    shape_specs = {
        'parallelogram': {
            'base': 8.0,
            'height': 4.5
        }
    }
    
    for shape_name, specs in shape_specs.items():
        base_val = specs['base']
        height_val = specs['height']
        calculated_area = get_parallelogram_area(base_val, height_val)
        print(calculated_area)