def flatten_and_find_max(nested_list):
    return max(max(sublist) for sublist in nested_list)

if __name__ == '__main__':
    sample = [[3, 5, 2], [8, 1, 9], [4, 7]]
    print(flatten_and_find_max(sample))