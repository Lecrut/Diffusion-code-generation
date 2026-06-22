def sort_three_bitwise(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError('All inputs must be numbers.')
    if a > b:
        a, b = (b, a)
    if a > c:
        a, c = (c, a)
    if b > c:
        b, c = (c, b)
    return [a, b, c]
if __name__ == '__main__':
    print(f'Sorting (1, 5, 3): {sort_three_bitwise(1, 5, 3)}')
    print(f'Sorting (10, -2, 7): {sort_three_bitwise(10, -2, 7)}')
    try:
        print(f"Sorting ('a', 5, 3): {sort_three_bitwise('a', 5, 3)}")
    except ValueError as e:
        print(f'Error caught: {e}')