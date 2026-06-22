def _validate_positive(val, name):
    if not isinstance(val, (int, float)):
        raise TypeError(f"{name} must be a number")
    if val <= 0:
        raise ValueError(f"{name} must be positive")
    return val

def get_prism_volume(base_area, height):
    validated_area = _validate_positive(base_area, "base_area")
    validated_height = _validate_positive(height, "height")
    return validated_area * validated_height

if __name__ == '__main__':
    sample_area = 50.0
    sample_h = 12.0
    computed_vol = get_prism_volume(sample_area, sample_h)
    print(computed_vol)