def flatten_and_find_max(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return max(flat_list)

if __name__ == '__main__':
    sample_list = [[1, 5], [3, 2], [9, 4]]
    print(f"Maximum value: {flatten_and_find_max(sample_list)}")