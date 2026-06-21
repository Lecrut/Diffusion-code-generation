def max_in_nested_list(nested_list):
    return max(max(sublist) for sublist in nested_list)

if __name__ == '__main__':
    sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(max_in_nested_list(sample))