def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid side lengths for a triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)