import math
def calculate_triangle_sides(a, b, c):
    hypotenuse = max(a, b, c)
    leg1 = min(a, b, c)
    leg2 = (a + b + c) - hypotenuse
    if hypotenuse * hypotenuse == leg1 * leg1 + leg2 * leg2:
        return leg1, leg2, hypotenuse
    else:
        return None
if __name__ == '__main__':
    leg_a = 3
    leg_b = 4
    hypotenuse_input = 5
    result = calculate_triangle_sides(leg_a, leg_b, hypotenuse_input)
    if result:
        print(f"Legs: {result[0]}, {result[1]}, Hypotenuse: {result[2]}")
    else:
        print("Invalid triangle dimensions provided.")