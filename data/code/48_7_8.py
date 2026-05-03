import math
def calculate_triangle_sides(a, b, c):
    if c > a and c > b:
        hypotenuse = c
        leg1 = a
        leg2 = b
    elif a > c and a > b:
        hypotenuse = a
        leg1 = c
        leg2 = b
    elif b > c and b > a:
        hypotenuse = b
        leg1 = c
        leg2 = a
    else:
        raise ValueError("Invalid side lengths provided. Hypotenuse must be the longest side.")
    if leg1 * leg1 + leg2 * leg2 == hypotenuse * hypotenuse:
        return leg1, leg2, hypotenuse
    else:
        raise ValueError("The provided sides do not form a right-angled triangle.")
if __name__ == '__main__':
    leg_a = 3
    leg_b = 4
    hypotenuse_c = 5
    try:
        result = calculate_triangle_sides(leg_a, leg_b, hypotenuse_c)
        print(f"Leg 1: {result[0]}")
        print(f"Leg 2: {result[1]}")
        print(f"Hypotenuse: {result[2]}")
    except ValueError as e:
        print(f"Error: {e}")
    leg_a_alt = 5
    leg_b_alt = 12
    hypotenuse_c_alt = 13
    try:
        result_alt = calculate_triangle_sides(leg_a_alt, leg_b_alt, hypotenuse_c_alt)
        print(f"Leg 1: {result_alt[0]}")
        print(f"Leg 2: {result_alt[1]}")
        print(f"Hypotenuse: {result_alt[2]}")
    except ValueError as e:
        print(f"Error: {e}")