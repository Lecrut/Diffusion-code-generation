def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_triangle_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("The given sides do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(f"The perimeter of the triangle with sides {side1}, {side2}, and {side3} is: {perimeter}")
    except ValueError as e:
        print(e)