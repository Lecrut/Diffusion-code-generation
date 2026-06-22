def get_side_length_and_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    area = side_length ** 2
    return (side_length, area)

if __name__ == '__main__':
    sample_values = [3, 5, 7]
    for value in sample_values:
        result = get_side_length_and_area(value)
        print(result)