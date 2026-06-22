SIDES_IN_SQUARE = 4

def calculate_perimeter(side_length):
    return side_length * SIDES_IN_SQUARE
if __name__ == '__main__':
    sample_side1 = 3
    result1 = calculate_perimeter(sample_side1)
    print(f'Perimeter for side length {sample_side1}: {result1}')
    sample_side2 = 10
    result2 = calculate_perimeter(sample_side2)
    print(f'Perimeter for side length {sample_side2}: {result2}')
    sample_side3 = 7
    result3 = calculate_perimeter(sample_side3)
    print(f'Perimeter for side length {sample_side3}: {result3}')