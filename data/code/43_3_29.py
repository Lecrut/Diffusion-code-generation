def square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    try:
        print(square_area(5))
    except ValueError as e:
        print(e)