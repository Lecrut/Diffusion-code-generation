SQUARE_SIDES_COUNT = 4

def calculate_perimeter(side_length):
    return side_length * SQUARE_SIDES_COUNT

if __name__ == '__main__':
    sample_side_length1 = 3
    result1 = calculate_perimeter(sample_side_length1)
    print(f"Perimeter for side length {sample_side_length1}: {result1}")
    
    sample_side_length2 = 5
    result2 = calculate_perimeter(sample_side_length2)
    print(f"Perimeter for side length {sample_side_length2}: {result2}")