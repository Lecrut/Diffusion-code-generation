def calculate_perimeter(a, b, c):
    if a + b > c and a + c > b and (b + c > a):
        return a + b + c
    else:
        raise ValueError('Invalid side lengths for a triangle')
if __name__ == '__main__':
    try:
        print(calculate_perimeter(3, 4, 5))
        print(calculate_perimeter(5, 5, 5))
        print(calculate_perimeter(2, 2, 4))
    except ValueError as e:
        print(e)