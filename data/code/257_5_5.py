def find_diff(nested_list):
    flat_list = [num for sublist in nested_list for num in sublist]
    return max(flat_list) - min(flat_list)

if __name__ == '__main__':
    sample_values = [[3, 5, 2], [8, 1, 9], [4, 7, 6]]
    print(find_diff(sample_values))