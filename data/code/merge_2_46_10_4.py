def find_unique_elements(input_list: list, reference_list: set) -> list:
    return [item for item in input_list if item not in reference_list]
if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample_reference = {4, 6, 8}
    result = find_unique_elements(sample_input, sample_reference)
    print(result)