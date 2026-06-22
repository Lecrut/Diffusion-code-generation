def get_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    side = 50
    print(get_square_area(side))