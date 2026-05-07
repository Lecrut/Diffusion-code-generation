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
    print("--- Test Case 1: a=True, b=False, c=False ---")
    check_conditions(True, False, False)
    print("\n--- Test Case 2: a=False, b=False, c=True ---")
    check_conditions(False, False, True)
    print("\n--- Test Case 3: a=True, b=True, c=False ---")
    check_conditions(True, True, False)
    print("\n--- Test Case 4: a=False, b=False, c=False ---")
    check_conditions(False, False, False)
    print("\n--- Test Case 5: a=True, b=True, c=True ---")
    check_conditions(True, True, True)