def calculate_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 10
    area = calculate_area(sample_side)
    print(area)