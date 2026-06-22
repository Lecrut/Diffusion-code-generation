def compute_square_area(side_length: float) -> float:
    return side_length * side_length

if __name__ == '__main__':
    print(compute_square_area(2.5))
    print(compute_square_area(7.12345678901234567890))
    print(compute_square_area(0.0))