import collections
def compare_sets(set1, set2):
    set1_list = list(set1)
    set2_list = list(set2)
    if set1 == set2:
        return "Sets are identical."
    elif set1.issubset(set2) and not set2.issubset(set1):
        return "Set1 is a proper subset of Set2."
    elif set2.issubset(set1) and not set1.issubset(set2):
        return "Set2 is a proper subset of Set1."
    else:
        diff1 = set1 - set2
        diff2 = set2 - set1
        if diff1 and diff2:
            return f"Sets have differing elements. Difference in Set1: {sorted(list(diff1))}, Difference in Set2: {sorted(list(diff2))}"
        elif diff1:
            return f"Set1 has elements not in Set2. Difference: {sorted(list(diff1))}"
        elif diff2:
            return f"Set2 has elements not in Set1. Difference: {sorted(list(diff2))}"
        else:
            return "Sets are equal (already covered by initial check, but for completeness)."
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
    print(f"Comparing Set E: {set_e} and Set A: {set_a}")
    result4 = compare_sets(set_e, set_a)
    print(result4)
    print("-" * 20)
    set_f = {10, 20}
    set_g = {10, 20, 30}
    print(f"Comparing Set F: {set_f} and Set G: {set_g}")
    result5 = compare_sets(set_f, set_g)
    print(result5)