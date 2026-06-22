def square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number")
    return side_length ** 2

if __name__ == '__main__':
    print(square_area(5))