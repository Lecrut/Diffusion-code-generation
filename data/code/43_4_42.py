def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    
    def validate_side_length(length: float) -> bool:
        return length >= 0

    if not validate_side_length(side_length):
        raise ValueError("Invalid side length")

    area = side_length * side_length
    return area

if __name__ == '__main__':
    sample_side_length = 4.5
    try:
        area = calculate_square_area(sample_side_length)
        print(f"The area of the square with side length {sample_side_length} is {area}")
    except ValueError as e:
        print(e)