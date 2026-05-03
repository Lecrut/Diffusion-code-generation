import math
def calculate_triangle_sides(a, b, c):
    hypotenuse = max(a, b, c)
    legs = [x for x in [a, b, c] if x != hypotenuse]
    if hypotenuse * hypotenuse == a * a + b * b or hypotenuse * hypotenuse == a * a + c * c or hypotenuse * hypotenuse == b * b + c * c:
        return a, b, c
    else:
        return None
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    hypotenuse = 5
    result = calculate_triangle_sides(leg1, leg2, hypotenuse)
    if result:
        print(f"Legs: {result[0]}, {result[1]}, Hypotenuse: {result[2]}")
    else:
        print("Invalid triangle sides provided.")