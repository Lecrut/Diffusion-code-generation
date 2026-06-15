def find_set_differences(A, B):
    set_A = set(A)
    set_B = set(B)
    common = set_A.intersection(set_B)
    only_in_A = set_A.difference(set_B)
    only_in_B = set_B.difference(set_A)
    return {
        'common': list(common),
        'only_in_A': list(only_in_A),
        'only_in_B': list(only_in_B)
    }
if __name__ == '__main__':
    list_A = [1, 2, 3, 4, 5, 6]
    list_B = [4, 5, 6, 7, 8, 9]
    result = find_set_differences(list_A, list_B)
    print(result)