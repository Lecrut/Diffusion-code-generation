def find_max_min_difference(nested_list):
    flattened_list = [num for sublist in nested_list for num in sublist]
    return max(flattened_list) - min(flattened_list)

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [2, 8, 4], [7, 6]]
    print(find_max_min_difference(sample_data))