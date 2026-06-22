UNIT_SCALE = {
    'mm': 1e-3,
    'cm': 1e-2,
    'm': 1.0,
    'km': 1e3,
    'in': 2.54e-2,
    'ft': 0.3048,
    'yd': 0.9144
}

def apply_scale(value, unit):
    if unit not in UNIT_SCALE:
        raise ValueError(f"Unknown unit: {unit}")
    return value * UNIT_SCALE[unit]

def prism_volume(base_area, height, base_unit='m', height_unit='m'):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative")
    scaled_base = apply_scale(base_area, base_unit)
    scaled_height = apply_scale(height, height_unit)
    return scaled_base * scaled_height

if __name__ == '__main__':
    area_val = 150
    height_val = 12
    unit_a = 'cm'
    unit_h = 'cm'
    result = prism_volume(area_val, height_val, unit_a, unit_h)
    print(result)