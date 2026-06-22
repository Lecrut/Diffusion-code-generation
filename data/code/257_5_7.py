def find_diff(nested_list):
    flat_list = [num for sublist in nested_list for num in sublist]
    return max(flat_list) - min(flat_list)

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [8, 2, 9], [4, 7, 6]]
    print(find_diff(sample_data))