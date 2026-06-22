def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    volume = float(base_area)
    volume *= float(height)
    return volume

if __name__ == '__main__':
    SAMPLE_DATA = {
        "pentagonal_prism": {"base_area": 42.5, "height": 15},
        "hexagonal_prism": {"base_area": 65.0, "height": 8.5}
    }
    
    for key in SAMPLE_DATA:
        data = SAMPLE_DATA[key]
        area = data["base_area"]
        h = data["height"]
        result = calculate_prism_volume(area, h)
        print(result)