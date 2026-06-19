def calculate_square_area(side: float) -> float:
    return side * side

if __name__ == '__main__':
    sample_side_length = 5.0
    area = calculate_square_area(sample_side_length)
    print(area)