def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Invalid input: side length must be an integer or float")
    return side_length * side_length

if __name__ == '__main__':
    area1 = calculate_square_area(5)
    print(f"Area of square with side 5: {area1}")
    
    area2 = calculate_square_area(10.5)
    print(f"Area of square with side 10.5: {area2}")