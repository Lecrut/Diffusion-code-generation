def get_unique_items(input_list):
    unique_set = set(input_list)
    return list(unique_set)
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
    unique_list = get_unique_items(sample_list)
    print(unique_list)