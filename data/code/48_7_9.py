import math
def calculate_triangle_sides(a, b, c):
    hypotenuse = max(a, b, c)
    legs = [x for x in [a, b, c] if x != hypotenuse]
    if hypotenuse == math.sqrt(legs[0]**2 + legs[1]**2):
        return a, b, c
    else:
        return a, b, c
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    hypotenuse = 5
    result = calculate_triangle_sides(leg1, leg2, hypotenuse)
    print(f"Legs: {result[0]}, {result[1]}, Hypotenuse: {result[2]}")