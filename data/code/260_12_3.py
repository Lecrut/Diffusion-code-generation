import collections
def compare_sets(set1, set2):
    set1_list = list(set1)
    set2_list = list(set2)
    if set1_list == set2_list:
        return "Sets are identical."
    elif len(set1_list) > len(set2_list):
        return "Set1 has more unique elements than Set2."
    else:
        return "Set2 has more unique elements than Set1."
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {3, 4, 5, 6, 7}
    print(f"Comparing Set A: {set_a}")
    print(f"Comparing Set B: {set_b}")
    result1 = compare_sets(set_a, set_b)
    print(f"Comparison Result 1: {result1}\n")
    set_c = {10, 20, 30}
    set_d = {10, 20, 30}
    print(f"Comparing Set C: {set_c}")
    print(f"Comparing Set D: {set_d}")
    result2 = compare_sets(set_c, set_d)
    print(f"Comparison Result 2: {result2}\n")
    set_e = {1, 2, 3}
    set_f = {1, 2}
    print(f"Comparing Set E: {set_e}")
    print(f"Comparing Set F: {set_f}")
    result3 = compare_sets(set_e, set_f)
    print(f"Comparison Result 3: {result3}\n")