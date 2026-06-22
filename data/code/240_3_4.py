def calculate_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 5
    area = calculate_area(sample_side_length)
    print(area)