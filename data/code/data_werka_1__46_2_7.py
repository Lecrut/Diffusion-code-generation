def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_perimeter(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        perimeter = calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)