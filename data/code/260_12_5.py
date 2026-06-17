import collections
def compare_sets(set1, set2):
    set1_list = list(set1)
    set2_list = list(set2)
    if set1_list == set2_list:
        return "The sets are identical."
    elif len(set1_list) > len(set2_list):
        return "Set 1 has more elements than Set 2."
    else:
        return "Set 2 has more elements than Set 1."
if __name__ == '__main__':
    set_a = {1, 5, 3, 7, 9}
    set_b = {3, 5, 7, 9, 10}
    result = compare_sets(set_a, set_b)
    print(result)
    set_c = {1, 2, 3}
    set_d = {1, 2, 3}
    result2 = compare_sets(set_c, set_d)
    print(result2)
    set_e = {10, 20}
    set_f = {10, 20, 30}
    result3 = compare_sets(set_e, set_f)
    print(result3)