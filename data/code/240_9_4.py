def calculate_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero")
    return side_length ** 2

if __name__ == '__main__':
    try:
        sample_side_length = 3
        area = calculate_area(sample_side_length)
        print(area)
    except ValueError as e:
        print(e)