def is_strict_superset(set1, set2):
    log = []
    log.append(f"Starting comparison between set1: {set1} and set2: {set2}")
    set1_unique = set(set1)
    set2_unique = set(set2)
    log.append(f"Set1 unique elements: {set1_unique}")
    log.append(f"Set2 unique elements: {set2_unique}")
    if set1_unique.issuperset(set2_unique):
        log.append("Result: True. Set1 is a superset of Set2.")
        if len(set1_unique) > len(set2_unique):
            log.append("Strictness check: True. Set1 has more unique elements than Set2.")
        else:
            log.append("Strictness check: False. Sets have the same number of unique elements (not a strict superset).")
        return True
    elif set1_unique == set2_unique:
        log.append("Result: False. Sets are equal, not a strict superset.")
        return False
    else:
        log.append("Result: False. Set1 is not a superset of Set2.")
        return False
if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {2, 3, 4}
    print("--- Test Case 1 ---")
    result1 = is_strict_superset(set_a, set_b)
    print(f"Final Result: {result1}\n")
    set_c = {1, 2, 3, 4}
    set_d = {1, 2, 3, 4}
    print("--- Test Case 2 (Equal Sets) ---")
    result2 = is_strict_superset(set_c, set_d)
    print(f"Final Result: {result2}\n")
    set_e = {1, 2, 3}
    set_f = {1, 2, 3, 4}
    print("--- Test Case 3 (Not a Superset) ---")
    result3 = is_strict_superset(set_e, set_f)
    print(f"Final Result: {result3}\n")
    set_g = {1, 2, 3, 4, 5}
    set_h = {1, 2, 3, 4}
    print("--- Test Case 4 (Strict Superset) ---")
    result4 = is_strict_superset(set_g, set_h)
    print(f"Final Result: {result4}\n")