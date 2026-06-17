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
        return "Sets are different."
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
    print(f"Comparing Set E: {set_e} and Set B: {set_b}")
    result4 = compare_sets(set_e, set_b)
    print(result4)
    print("-" * 20)
    print(f"Comparing Set A: {set_a} and Set E: {set_e}")
    result5 = compare_sets(set_a, set_e)
    print(result5)
    print("-" * 20)