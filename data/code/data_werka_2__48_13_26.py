import math

def calculate_triangle_properties(base, height):
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    area = 0.5 * base * height
    return (hypotenuse, area)
if __name__ == '__main__':
    base_length = 6.0
    height_length = 8.0
    hypotenuse, area = calculate_triangle_properties(base_length, height_length)
    print(f'Hypotenuse: {hypotenuse}')
    print(f'Area: {area}')