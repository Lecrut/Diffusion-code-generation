def get_side_length_and_area(side_length):
    area = side_length * side_length
    return (side_length, area)

if __name__ == '__main__':
    sample_values = [5, 10.5]
    for value in sample_values:
        result = get_side_length_and_area(value)
        print(result)