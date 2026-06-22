def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be an integer or float")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    area1 = calculate_area(5)
    print(f"Area of square with side length 5: {area1}")
    
    area2 = calculate_area(10.5)
    print(f"Area of square with side length 10.5: {area2}")