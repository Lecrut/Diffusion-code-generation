def validate_input(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be integers or floats.")

def compare_adjacent_numbers(data):
    validate_input(data)
    return [data[i] < data[i + 1] for i in range(len(data) - 1)]

if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4]
    sample_data_2 = [4, 3, 2, 1]
    sample_data_3 = [1.5, 2.0, 2.5, 3.0]
    sample_data_4 = [1, 'a', 3, 4]

    print("Sample Data 1:", compare_adjacent_numbers(sample_data_1))
    try:
        print("Sample Data 2:", compare_adjacent_numbers(sample_data_2))
    except TypeError as e:
        print("Error:", e)
    print("Sample Data 3:", compare_adjacent_numbers(sample_data_3))
    try:
        print("Sample Data 4:", compare_adjacent_numbers(sample_data_4))
    except TypeError as e:
        print("Error:", e)