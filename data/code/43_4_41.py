def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    SQUARE_MULTIPLIER = 2
    half_side_length = side_length / SQUARE_MULTIPLIER
    return half_side_length * (side_length - half_side_length)
if __name__ == '__main__':
    sample_side_length = 4.0
    area = calculate_square_area(sample_side_length)
    print(area)