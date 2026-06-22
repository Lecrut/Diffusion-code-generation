def calculate_perimeter(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero")
    return 4 * side_length

if __name__ == '__main__':
    sample_side1 = 3
    result1 = calculate_perimeter(sample_side1)
    print(f"Perimeter for {sample_side1}: {result1}")
    sample_side2 = 10
    result2 = calculate_perimeter(sample_side2)
    print(f"Perimeter for {sample_side2}: {result2}")
    sample_side3 = 7
    result3 = calculate_perimeter(sample_side3)
    print(f"Perimeter for {sample_side3}: {result3}")