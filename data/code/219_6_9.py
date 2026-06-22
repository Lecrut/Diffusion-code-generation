def flatten_and_max(nested_list):
    return max(sum(sublist, []) for sublist in nested_list)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], 6], 7]
    print(flatten_and_max(sample_data))