def calculate_perimeter(side_length):
    perimeter = 4 * side_length
    return perimeter

if __name__ == '__main__':
    sample_side1 = 3
    result1 = calculate_perimeter(sample_side1)
    print(f"Perimeter for side length {sample_side1}: {result1}")
    
    sample_side2 = 5
    result2 = calculate_perimeter(sample_side2)
    print(f"Perimeter for side length {sample_side2}: {result2}")