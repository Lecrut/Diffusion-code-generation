def calculate_square_area(side_length):
    try:
        length = float(side_length)
        if length < 0:
            raise ValueError("Side length must be non-negative")
        return length * length
    except (TypeError, ValueError) as e:
        if isinstance(e, ValueError) and "could not convert" in str(e):
            raise ValueError("Input must be a numeric value")
        raise

if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(3.5))
    try:
        calculate_square_area("abc")
    except ValueError as e:
        print(e)
    try:
        calculate_square_area(-2)
    except ValueError as e:
        print(e)