import math

calculate_triangle_area = lambda base, height: (base * height) / 2

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = calculate_triangle_area(base_value, height_value)
    print(result)