def compute_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length * side_length

if __name__ == '__main__':
    print(compute_square_area(5))
    print(compute_square_area(0))
    try:
        print(compute_square_area(-3))
    except ValueError as e:
        print(str(e))