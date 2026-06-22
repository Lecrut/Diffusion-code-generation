def validate_side_length(side_length):
    if not isinstance(side_length, int) or side_length <= 0:
        raise ValueError("Side length must be a positive integer")

def calculate_square_perimeter(side_length):
    validate_side_length(side_length)
    return 4 * side_length

if __name__ == '__main__':
    sample1 = 5
    result1 = calculate_square_perimeter(sample1)
    print(f"Perimeter of square with side {sample1}: {result1}")
    
    sample2 = 3
    result2 = calculate_square_perimeter(sample2)
    print(f"Perimeter of square with side {sample2}: {result2}")