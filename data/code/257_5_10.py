def find_difference(nested_list):
    flat_list = [num for sublist in nested_list for num in sublist]
    return max(flat_list) - min(flat_list)

if __name__ == '__main__':
    sample_values = [[3, 5, 1], [8, 2], [4]]
    print(find_difference(sample_values))