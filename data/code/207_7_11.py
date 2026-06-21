def max_in_nested_list(nested_list):
    return max(max(sublist) for sublist in nested_list)

if __name__ == '__main__':
    sample = [[3, 5, 2], [8, 1], [4, 9]]
    print(max_in_nested_list(sample))