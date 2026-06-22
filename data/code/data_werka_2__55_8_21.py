def calculate_triangle_perimeter(a, b, c):
    side_lengths = {'a': a, 'b': b, 'c': c}
    for side, length in side_lengths.items():
        if length <= 0:
            raise ValueError(f"Side {side} must be a positive number.")
    return sum(side_lengths.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(7, 10, 5)
        print(perimeter)
    except ValueError as e:
        print(e)