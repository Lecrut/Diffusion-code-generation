def square_area(side):
    if not isinstance(side, int) or side < 0:
        raise ValueError("Side must be a non-negative integer")
    return side * side

if __name__ == '__main__':
    side_length = 5
    result = square_area(side_length)
    print(result)