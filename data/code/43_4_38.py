def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError('Side length cannot be negative')

    def multiply(a: float, b: float) -> float:
        return a * b
    return multiply(side_length, side_length)
if __name__ == '__main__':
    sample_side_length = 3.0
    area = calculate_square_area(sample_side_length)
    print(area)