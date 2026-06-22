def calculate_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    print(calculate_area(5))
    print(calculate_area(7.5))
    try:
        print(calculate_area(-3))
    except ValueError as e:
        print(e)