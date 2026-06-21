def extract_max_from_nested_list(nested_list):
    flattened = [item for sublist in nested_list for item in sublist]
    return max(flattened)

if __name__ == '__main__':
    sample_values = [[1, 5], [3, 2], [9, 4]]
    print(extract_max_from_nested_list(sample_values))