def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid triangle sides')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)