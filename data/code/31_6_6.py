def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(0))
    try:
        calculate_square_area(-5)
    except ValueError as e:
        print(f"Error: {e}")