def _validate_dims(area, h):
    if area < 0 or h < 0:
        raise ValueError
    return True

def calculate_prism_volume(base_area, height):
    _validate_dims(base_area, height)
    return base_area * height

if __name__ == '__main__':
    b = 12.0
    h = 8.0
    print(calculate_prism_volume(b, h))