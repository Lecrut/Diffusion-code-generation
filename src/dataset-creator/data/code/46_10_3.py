def find_unique_values(input_list: list, reference_list: set) -> list:
    return [item for item in input_list if item not in reference_list]
if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    reference_data = {1, 3, 5, 7, 9, 11, 13}
    result = find_unique_values(sample_input, reference_data)
    print(result)