def square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5
    print(square_area(sample_side))