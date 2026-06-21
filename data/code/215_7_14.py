def extract_max_from_nested_list(nested_list):
    flattened_list = [item for sublist in nested_list for item in sublist]
    return max(flattened_list)

if __name__ == '__main__':
    sample_list = [[1, 5], [3, 2], [9, 4]]
    print(extract_max_from_nested_list(sample_list))