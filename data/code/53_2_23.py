def get_side_length_and_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    area = side_length * side_length
    return (side_length, area)

if __name__ == '__main__':
    sample_values = [2.5, 4, 6]
    for value in sample_values:
        try:
            result = get_side_length_and_area(value)
            print(result)
        except ValueError as e:
            print(e)