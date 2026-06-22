def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    area = 25.0
    h = 10.0
    result = calculate_prism_volume(area, h)
    print(result)