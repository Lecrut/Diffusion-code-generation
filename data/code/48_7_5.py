import math
def calculate_triangle_sides(a, b, c):
    hypotenuse = max(a, b, c)
    legs = [x for x in [a, b, c] if x != hypotenuse]
    if hypotenuse * hypotenuse == a * a + b * b:
        return a, b, c
    else:
        calculated_hypotenuse = math.sqrt(a**2 + b**2)
        return a, b, calculated_hypotenuse
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    hypotenuse_input = 5.0
    result = calculate_triangle_sides(leg1, leg2, hypotenuse_input)
    print(f"Leg 1: {result[0]}")
    print(f"Leg 2: {result[1]}")
    print(f"Hypotenuse: {result[2]}")