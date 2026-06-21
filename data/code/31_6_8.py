def calculate_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length * side_length

if __name__ == '__main__':
    print(calculate_area(5))
    print(calculate_area(10))
    try:
        calculate_area(-2)
    except ValueError as e:
        print(e)