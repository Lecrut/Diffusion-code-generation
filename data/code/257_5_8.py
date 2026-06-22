def find_max_min_difference(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return max(flat_list) - min(flat_list)

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [8, 2], [4]]
    print(find_max_min_difference(sample_data))