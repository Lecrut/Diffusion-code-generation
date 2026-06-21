def calculate_triangle_perimeter(a, b, c):
    side_lengths = {'a': a, 'b': b, 'c': c}
    for key, value in side_lengths.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f'Side {key} must be a number.')
        if value <= 0:
            raise ValueError(f'Side {key} must be positive.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(10, 10, 10))
        print(calculate_triangle_perimeter(1, 1, 2))
    except Exception as e:
        print(e)