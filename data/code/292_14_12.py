def calculate_square_perimeter(side_length):
    if not isinstance(side_length, int) or side_length <= 0:
        raise ValueError("Side length must be a positive integer.")
    return side_length * 4

if __name__ == '__main__':
    sample1 = 5
    result1 = calculate_square_perimeter(sample1)
    print(f"Perimeter of square with side {sample1}: {result1}")
    sample2 = 8
    result2 = calculate_square_perimeter(sample2)
    print(f"Perimeter of square with side {sample2}: {result2}")
    sample3 = -3
    try:
        result3 = calculate_square_perimeter(sample3)
    except ValueError as e:
        print(e)