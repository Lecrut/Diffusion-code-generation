def is_valid_side_length(side_length: float) -> bool:
    return side_length >= 0

def calculate_square_area(side_length: float) -> float:
    if not is_valid_side_length(side_length):
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4.5
    area = calculate_square_area(sample_side_length)
    print(area)