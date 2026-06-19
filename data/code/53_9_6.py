def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side_length ** 2

if __name__ == '__main__':
    sample_sizes = {
        'tiny': 1,
        'small': 3,
        'medium': 5,
        'large': 10,
        'huge': 20
    }
    for size, value in sample_sizes.items():
        area = calculate_square_area(value)
        print(f"The area of a {size} square with side length {value} is {area}.")