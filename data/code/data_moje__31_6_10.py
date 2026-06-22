def square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    print(square_area(5))
    print(square_area(0))
    try:
        square_area(-1)
    except ValueError as e:
        print(f"Error: {e}")