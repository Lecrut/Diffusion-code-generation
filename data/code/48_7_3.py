import math
def calculate_triangle_sides(a, b, c):
    hypotenuse = max(a, b, c)
    legs = [x for x in [a, b, c] if x != hypotenuse]
    if hypotenuse * hypotenuse == leg1 * leg1 + leg2 * leg2:
        return leg1, leg2, hypotenuse
    else:
        return None, None, None
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    hypotenuse = 5
    result_a, result_b, result_c = calculate_triangle_sides(leg1, leg2, hypotenuse)
    if result_a is not None:
        print(f"Legs: {result_a}, {result_b}, Hypotenuse: {result_c}")
    else:
        print("Invalid triangle configuration.")