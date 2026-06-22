def calculate_perimeter(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return 4 * side_length

if __name__ == '__main__':
    sample_side_length = 9
    perimeter = calculate_perimeter(sample_side_length)
    print(perimeter)