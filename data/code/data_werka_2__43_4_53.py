def validate_side_length(side_length: float) -> None:
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length: float) -> float:
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4.5
    area = calculate_square_area(sample_side_length)
    print(area)