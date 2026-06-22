def validate_side_length(side):
    if not isinstance(side, int) or side <= 0:
        return False
    return True

def calculate_square_perimeter(side_length):
    if not validate_side_length(side_length):
        raise ValueError("Side length must be a positive integer.")
    return 4 * side_length

if __name__ == '__main__':
    sample1 = 5
    result1 = calculate_square_perimeter(sample1)
    print(f"Perimeter of square with side {sample1}: {result1}")
    
    sample2 = 8
    result2 = calculate_square_perimeter(sample2)
    print(f"Perimeter of square with side {sample2}: {result2}")