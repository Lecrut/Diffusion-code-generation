def calculate_parallelogram_area(base, height):
    base_value = float(base)
    height_value = float(height)
    product = base_value * height_value
    return product

BASE = 15.5
HEIGHT = 4.2

if __name__ == '__main__':
    result = calculate_parallelogram_area(BASE, HEIGHT)
    print(result)