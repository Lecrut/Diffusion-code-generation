def find_set_differences(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    common = set_a.intersection(set_b)
    only_in_a = set_a.difference(set_b)
    only_in_b = set_b.difference(set_a)
    return {
        'common': list(common),
        'only_in_A': list(only_in_a),
        'only_in_B': list(only_in_b)
    }
if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5, 6]
    list_b_sample = [4, 5, 6, 7, 8, 9]
    result = find_set_differences(list_a_sample, list_b_sample)
    print(result)