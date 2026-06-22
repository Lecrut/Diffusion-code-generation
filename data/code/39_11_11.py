def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    result1 = calculate_prism_volume(10, 5)
    print(result1)
    result2 = calculate_prism_volume(24.5, 3.2)
    print(result2)
    result3 = calculate_prism_volume(0, 100)
    print(result3)