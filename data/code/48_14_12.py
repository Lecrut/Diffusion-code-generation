def calculate_hypotenuse(base, height):
    return (base ** 2 + height ** 2) ** 0.5

def calculate_area(base, height):
    return 0.5 * base * height

def is_right_triangle(base, height, hypotenuse):
    return abs(hypotenuse ** 2 - (base ** 2 + height ** 2)) < 1e-09
if __name__ == '__main__':
    base = 6.0
    height = 8.0
    if base <= 0 or height <= 0:
        print('Base and height must be positive numbers.')
    else:
        hypotenuse = calculate_hypotenuse(base, height)
        area = calculate_area(base, height)
        if is_right_triangle(base, height, hypotenuse):
            print(f'Hypotenuse: {hypotenuse}')
            print(f'Area: {area}')
        else:
            print('The given dimensions do not form a right-angled triangle.')