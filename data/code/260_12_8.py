import collections
def compare_sets(set1, set2):
    set1_list = list(set1)
    set2_list = list(set2)
    if set1_list == set2_list:
        return "The sets are identical."
    elif len(set1_list) > len(set2_list):
        return "Set 1 has more unique elements than Set 2."
    else:
        return "Set 2 has more unique elements than Set 1."
if __name__ == '__main__':
    set_a = {1, 5, 3, 8, 5}
    set_b = {3, 5, 8, 9, 1}
    result = compare_sets(set_a, set_b)
    print(result)