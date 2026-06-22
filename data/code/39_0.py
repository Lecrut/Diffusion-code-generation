def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 10
    h = 5
    result = calculate_prism_volume(base, h)
    print(result)