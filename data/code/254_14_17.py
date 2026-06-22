def find_min_in_nested_list(nested_list):
    flattened = [item for sublist in nested_list for item in sublist]
    return min(flattened)

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [2, 8], [4]]
    print(find_min_in_nested_list(sample_data))