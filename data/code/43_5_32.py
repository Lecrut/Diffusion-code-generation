def compute_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length * side_length

if __name__ == '__main__':
    try:
        sample_side_length = 8
        area = compute_area(sample_side_length)
        print(area)
    except ValueError as e:
        print(e)