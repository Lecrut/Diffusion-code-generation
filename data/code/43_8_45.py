def calculate_square_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2

if __name__ == '__main__':
    try:
        sample_side = 7
        print(calculate_square_area(sample_side))
    except ValueError as e:
        print(e)