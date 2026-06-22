def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)