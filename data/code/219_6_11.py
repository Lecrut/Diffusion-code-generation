def flatten_and_find_max(nested_list):
    return max(max(sublist) for sublist in nested_list)

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [8, 2], [9]]
    print(flatten_and_find_max(sample_data))