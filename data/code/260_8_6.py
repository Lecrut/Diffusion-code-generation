def is_strict_superset(set1, set2):
    log = []
    log.append(f"Starting comparison between set1: {set1} and set2: {set2}")
    if set1 is None or set2 is None:
        log.append("Error: One or both sets are None.")
        return False
    set1_unique = set(set1)
    set2_unique = set(set2)
    log.append(f"Set 1 unique elements: {set1_unique}")
    log.append(f"Set 2 unique elements: {set2_unique}")
    if set1_unique.issuperset(set2_unique):
        log.append("Result: True. Set 1 is a superset of Set 2.")
        return True
    else:
        log.append("Result: False. Set 1 is not a superset of Set 2.")
        return False
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {2, 4, 6, 8}
    set_c = {1, 2, 3, 4, 5}
    set_d = {1, 2, 3, 4, 5, 6}
    set_e = {1, 2, 3, 4, 5}
    print("--- Comparison 1: A vs B ---")
    result1 = is_strict_superset(set_a, set_b)
    print(f"Final Result: {result1}\n")
    print("--- Comparison 2: C vs A (Testing strictness where sets are equal) ---")
    result2 = is_strict_superset(set_c, set_a)
    print(f"Final Result: {result2}\n")
    print("--- Comparison 3: D vs A (Testing superset relationship) ---")
    result3 = is_strict_superset(set_d, set_a)
    print(f"Final Result: {result3}\n")
    print("--- Comparison 4: E vs A (Testing equality) ---")
    result4 = is_strict_superset(set_e, set_a)
    print(f"Final Result: {result4}\n")