def combine_lists(list_one, list_two):
    combined_set = set(list_one)
    combined_set.update(list_two)
    return list(combined_set)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = combine_lists(list_a, list_b)
    print(result)