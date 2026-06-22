def _validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value

def get_prism_volume(base_area, height):
    safe_base = _validate_positive(base_area, "base_area")
    safe_height = _validate_positive(height, "height")
    return safe_base * safe_height

if __name__ == '__main__':
    test_base = 36
    test_height = 8
    final_volume = get_prism_volume(test_base, test_height)
    print(final_volume)