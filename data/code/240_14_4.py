def calculate_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number")
    return float(side_length ** 2)

if __name__ == '__main__':
    sample_side = 5.5
    area = calculate_area(sample_side)
    print(area)