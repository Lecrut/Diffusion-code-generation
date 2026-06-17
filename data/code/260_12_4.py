import collections
def compare_sets(set1, set2):
    set1_list = list(set1)
    set2_list = list(set2)
    if set1 == set2:
        return "Sets are identical."
    elif set1.issubset(set2):
        return "Set1 is a subset of Set2 (Set2 has extra elements)."
    elif set2.issubset(set1):
        return "Set2 is a subset of Set1 (Set1 has extra elements)."
    else:
        diff1 = set1 - set2
        diff2 = set2 - set1
        return f"Sets are different. Difference (Set1 only): {sorted(list(diff1))}. Difference (Set2 only): {sorted(list(diff2))}"
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {3, 4, 5, 6, 7}
    set_c = {1, 2, 3, 4, 5}
    set_d = {1, 2, 3}
    set_e = {1, 2, 3, 4, 5}
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
    print(f"Comparing Set E: {set_e} and Set E: {set_e}")
    result4 = compare_sets(set_e, set_e)
    print(result4)
    print("-" * 20)
    print(f"Comparing Set A: {set_a} and Set D: {set_d}")
    result5 = compare_sets(set_a, set_d)
    print(result5)
    print("-" * 20)