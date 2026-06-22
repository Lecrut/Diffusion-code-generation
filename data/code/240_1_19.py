def calculate_square_area(side_length: int) -> int:
    area = side_length * side_length
    return area

if __name__ == '__main__':
    sample_side1 = 8
    result1 = calculate_square_area(sample_side1)
    print(f"The area of a square with side {sample_side1} is: {result1}")
    
    sample_side2 = 12
    result2 = calculate_square_area(sample_side2)
    print(f"The area of a square with side {sample_side2} is: {result2}")