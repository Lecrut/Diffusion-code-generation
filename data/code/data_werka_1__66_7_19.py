def validate_data(data):
    if not all((isinstance(x, (int, float)) for x in data)):
        raise TypeError('All elements must be integers or floats.')

def compare_adjacent_ascending(data):
    validate_data(data)
    return [data[i] < data[i + 1] for i in range(len(data) - 1)]
if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4]
    sample_data_2 = [4, 3, 2, 1]
    sample_data_3 = [1.5, 2.0, 2.5, 3.0]
    sample_data_4 = [1, 'a', 2, 3]
    try:
        print(compare_adjacent_ascending(sample_data_1))
        print(compare_adjacent_ascending(sample_data_2))
        print(compare_adjacent_ascending(sample_data_3))
    except TypeError as e:
        print(e)