def find_matching_pair_generator(list1, list2):
    for val1 in list1:
        for val2 in list2:
            if val1 == val2:
                yield True
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    matching_pairs = find_matching_pair_generator(list_a, list_b)
    results = list(matching_pairs)
    print(results)