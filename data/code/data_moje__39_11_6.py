def calculate_prism_volume(base_area, height):
    if base_area <= 0 or height <= 0:
        return 0
    return base_area * height

if __name__ == '__main__':
    result = calculate_prism_volume(10, 5)
    print(result)
    result2 = calculate_prism_volume(20, 10)
    print(result2)
    result3 = calculate_prism_volume(15, 3)
    print(result3)