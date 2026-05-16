def check_conditions(a, b, c):
    if a or b:
        print("Condition 1: True (a or b is True)")
    if not (c or a):
        print("Condition 2: True (not (c or a) is True)")
    if a or b or c:
        print("Condition 3: True (a or b or c is True)")
    else:
        print("Condition 3: False (a or b or c is False)")
if __name__ == '__main__':
    value1 = True
    value2 = False
    value3 = True
    print("--- Test Case 1: (True or False) ---")
    check_conditions(value1, value2, value3)
    print("\n--- Test Case 2: (False or False) ---")
    check_conditions(False, False, False)
    print("\n--- Test Case 3: (True or True) ---")
    check_conditions(True, True, False)
    print("\n--- Test Case 4: (False or True) ---")
    check_conditions(False, True, False)