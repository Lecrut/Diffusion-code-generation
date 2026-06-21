def flatten_and_find_max(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return max(flat_list)

if __name__ == '__main__':
    sample_lists = [
        [[1, 5], [3, 2], [9, 4]],
        [[-100, -5, -1000], [-1, -2, -3]],
        [[0, 0, 0], [0]],
        [[999999999999999999999, 1000000000000000000000, 500000000000000000000]]
    ]
    for lst in sample_lists:
        print(f"Largest in {lst}: {flatten_and_find_max(lst)}")