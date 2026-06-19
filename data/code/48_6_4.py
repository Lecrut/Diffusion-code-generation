import math

def calculate_triangle_sides(leg1, leg2):
    hypotenuse = math.sqrt(leg1**2 + leg2**2)
    return (leg1, leg2, hypotenuse)

if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    sides = calculate_triangle_sides(leg1, leg2)
    print(sides)