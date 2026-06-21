def compute_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [3, 5.5, -1, 'a']
    for value in sample_values:
        try:
            area = compute_square_area(value)
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(f"Error: {e}")