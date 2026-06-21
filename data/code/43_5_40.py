def compute_square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length * side_length

if __name__ == '__main__':
    sample_side_length = 3
    area = compute_square_area(sample_side_length)
    print(area)