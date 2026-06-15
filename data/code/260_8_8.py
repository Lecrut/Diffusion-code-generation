def is_strict_superset(set1, set2):
    log = []
    log.append(f"Starting comparison between set1: {set1} and set2: {set2}")
    set1_unique = set(set1)
    set2_unique = set(set2)
    log.append(f"Set1 unique elements: {set1_unique}")
    log.append(f"Set2 unique elements: {set2_unique}")
    if set1_unique.issuperset(set2_unique):
        log.append("Result: True. Set1 is a superset of Set2.")
        return True
    elif set1_unique != set2_unique:
        log.append("Result: False. Sets are not equal, and Set1 is not a superset of Set2.")
        return False
    else:
        log.append("Result: False. Sets are equal, so Set1 is not a *strict* superset of Set2.")
        return False
if __name__ == '__main__':
    set_a = {1, 2, 3, 4}
    set_b = {1, 2, 3}
    set_c = {1, 2, 3, 4}
    set_d = {1, 2, 5}
    set_e = {1, 2, 3, 4, 5}
    print("--- Comparison 1: A vs B ---")
    result1 = is_strict_superset(set_a, set_b)
    print(f"Final Result: {result1}\n")
    print("--- Comparison 2: C vs A (Equality case) ---")
    result2 = is_strict_superset(set_c, set_a)
    print(f"Final Result: {result2}\n")
    print("--- Comparison 3: D vs A (Not a superset) ---")
    result3 = is_strict_superset(set_d, set_a)
    print(f"Final Result: {result3}\n")
    print("--- Comparison 4: E vs A (Superset case) ---")
    result4 = is_strict_superset(set_e, set_a)
    print(f"Final Result: {result4}\n")