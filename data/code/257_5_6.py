def find_diff(nested_list):
    flat_list = [num for sublist in nested_list for num in sublist]
    return max(flat_list) - min(flat_list)

if __name__ == '__main__':
    sample_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(find_diff(sample_values))