def get_side_length_and_area(side_length):
    area = side_length ** 2
    return (side_length, area)

if __name__ == '__main__':
    sample_values = [3, 5, 7]
    results = [get_side_length_and_area(value) for value in sample_values]
    print(results)