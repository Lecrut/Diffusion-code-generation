def combine_unique(list_a, list_b):
    combined_set = set(list_a)
    combined_set.update(list_b)
    return list(combined_set)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = combine_unique(list_a, list_b)
    print(result)