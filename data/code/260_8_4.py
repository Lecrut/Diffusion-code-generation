def is_strict_superset(set1, set2):
    log = []
    log.append("Starting comparison between set1 and set2.")
    set1_unique = set(set1)
    set2_unique = set(set2)
    log.append(f"Set 1 unique elements: {set1_unique}")
    log.append(f"Set 2 unique elements: {set2_unique}")
    if set1_unique.issuperset(set2_unique):
        log.append("Result: True. Set 1 is a superset of Set 2.")
        if len(set1_unique) > len(set2_unique):
            log.append("Detail: Set 1 has more unique elements than Set 2.")
        else:
            log.append("Detail: Set 1 and Set 2 have the same number of unique elements (which implies equality if it's a superset).")
        return True
    elif set1_unique == set2_unique:
        log.append("Result: False. Sets are equal, not a strict superset.")
        return False
    else:
        log.append("Result: False. Set 1 is not a superset of Set 2.")
        return False
if __name__ == '__main__':
    A = {1, 2, 3, 4}
    B = {2, 3, 4}
    C = {1, 2, 3, 4}
    D = {5, 6}
    E = {1, 2, 3, 4, 5}
    print("--- Comparison 1: A vs B ---")
    result1 = is_strict_superset(A, B)
    print(f"Final Boolean Result: {result1}\n")
    print("--- Comparison 2: C vs A (Equality Check) ---")
    result2 = is_strict_superset(C, A)
    print(f"Final Boolean Result: {result2}\n")
    print("--- Comparison 3: D vs A (Not a Superset) ---")
    result3 = is_strict_superset(D, A)
    print(f"Final Boolean Result: {result3}\n")
    print("--- Comparison 4: E vs B (Strict Superset Check) ---")
    result4 = is_strict_superset(E, B)
    print(f"Final Boolean Result: {result4}\n")