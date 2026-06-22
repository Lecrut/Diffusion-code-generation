def compute_prism_volume(base_area, height):
    if not isinstance(base_area, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError('Base area and height must be numeric')
    if base_area < 0 or height < 0:
        raise ValueError('Base area and height must be non-negative')
    return base_area * height
if __name__ == '__main__':
    base_area = 10.5
    height = 5.0
    volume = compute_prism_volume(base_area, height)
    print(volume)