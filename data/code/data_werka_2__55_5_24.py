def validate_sides(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid triangle sides")

def calculate_perimeter(a, b, c):
    validate_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    side1 = 6
    side2 = 8
    side3 = 10
    try:
        perimeter = calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)