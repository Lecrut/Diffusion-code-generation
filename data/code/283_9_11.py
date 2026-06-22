def count_non_matching_elements(data, data_type):
    return sum((1 for element in data if not isinstance(element, data_type)))
if __name__ == '__main__':
    sample_data = [1.5, 2.3, 4, True, 'hello', 7]
    print(count_non_matching_elements(sample_data, float))