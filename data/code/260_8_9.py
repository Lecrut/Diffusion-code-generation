def is_strict_superset(set1, set2):
    log = []
    log.append(f"Starting comparison: set1={set1}, set2={set2}")
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
    set_a = {1, 2, 3, 4}
    set_b = {2, 3, 4, 5, 6}
    print("--- Comparison 1 ---")
    result1 = is_strict_superset(set_a, set_b)
    print(f"Final Result: {result1}\n")
    set_c = {1, 2, 3, 4, 5}
    set_d = {1, 2, 3, 4}
    print("--- Comparison 2 ---")
    result2 = is_strict_superset(set_c, set_d)
    print(f"Final Result: {result2}\n")
    set_e = {1, 2}
    set_f = {1, 2, 3}
    print("--- Comparison 3 ---")
    result3 = is_strict_superset(set_e, set_f)
    print(f"Final Result: {result3}\n")