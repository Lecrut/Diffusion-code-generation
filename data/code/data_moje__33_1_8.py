def get_unit_info(unit_name):
    units = {
        'cm': {'scale': 1, 'name': 'centimeters'},
        'm': {'scale': 100, 'name': 'meters'},
        'km': {'scale': 100000, 'name': 'kilometers'},
        'in': {'scale': 2.54, 'name': 'inches'}
    }
    return units.get(unit_name, units['cm'])

def compute_triangle_area(base, height, unit='cm'):
    info = get_unit_info(unit)
    base_scaled = base * info['scale']
    height_scaled = height * info['scale']
    area_scaled = 0.5 * base_scaled * height_scaled
    area = area_scaled / (info['scale'] * info['scale'])
    return area

if __name__ == '__main__':
    base_val = 12.5
    height_val = 7.2
    unit_val = 'cm'
    result = compute_triangle_area(base_val, height_val, unit_val)
    print(result)