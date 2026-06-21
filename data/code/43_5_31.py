def compute_area_of_square(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length * side_length

if __name__ == '__main__':
    sample_side_lengths = {
        'small': 3,
        'medium': 5,
        'large': 7
    }
    for size, length in sample_side_lengths.items():
        print(f"The area of a {size} square with side length {length} is {compute_area_of_square(length)}")