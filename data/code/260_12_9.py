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
    set_a = {1, 2, 3, 4, 5}
    set_b = {3, 4, 5, 6, 7}
    set_c = {1, 2, 3, 4, 5}
    set_d = {1, 2, 3}
    print(f"Comparing Set A: {set_a} and Set B: {set_b}")
    result1 = compare_sets(set_a, set_b)
    print(result1)
    print("-" * 20)
    print(f"Comparing Set A: {set_a} and Set C: {set_c}")
    result2 = compare_sets(set_a, set_c)
    print(result2)
    print("-" * 20)
    print(f"Comparing Set D: {set_d} and Set A: {set_a}")
    result3 = compare_sets(set_d, set_a)
    print(result3)
    print("-" * 20)