def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_side_length = 7.5
    area = calculate_square_area(sample_side_length)
    print(area)