def flatten_and_find_max(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return max(flat_list)
if __name__ == '__main__':
    sample_list = [[3, 4, 5], [1, 2], [6, 7]]
    maximum = flatten_and_find_max(sample_list)
    print(maximum)
    sample_list_2 = [[-1, -2, -3], [-4, -5], [-6, -7, -8, -9]]
    maximum_2 = flatten_and_find_max(sample_list_2)
    print(maximum_2)