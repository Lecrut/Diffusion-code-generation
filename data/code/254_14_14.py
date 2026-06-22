def find_min_in_nested_list(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return min(flat_list)

if __name__ == '__main__':
    sample_list = [[3, 5, 1], [2, 8], [4]]
    print(find_min_in_nested_list(sample_list))