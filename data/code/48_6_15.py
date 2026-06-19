import math

def calculate_triangle_sides(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return {'leg1': a, 'leg2': b, 'hypotenuse': c}
if __name__ == '__main__':
    sample_leg1 = 3
    sample_leg2 = 4
    triangle_sides = calculate_triangle_sides(sample_leg1, sample_leg2)
    print(triangle_sides)