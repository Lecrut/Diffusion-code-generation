def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area = 50
    height = 12
    result = calculate_prism_volume(base_area, height)
    print(result)