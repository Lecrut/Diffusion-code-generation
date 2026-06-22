def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be a numeric value (int or float)")
    if side_length < 0:
        raise ValueError("side_length must be non-negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5
    result = calculate_square_area(sample_side)
    print(result)
    sample_side_float = 4.5
    result_float = calculate_square_area(sample_side_float)
    print(result_float)
    try:
        calculate_square_area(-3)
    except ValueError as e:
        print(e)
    try:
        calculate_square_area("text")
    except TypeError as e:
        print(e)