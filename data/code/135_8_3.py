def check_equivalence(a, b, c):
    result1 = (a > b) or (c == 10)
    result2 = (a > b) or (c == 10)
    return result1 == result2
if __name__ == '__main__':
    test_cases = [
        (5, 3, 10),
        (5, 3, 5),
        (1, 2, 10),
        (1, 2, 5)
    ]
    all_equivalent = True
    for a, b, c in test_cases:
        is_equivalent = check_equivalence(a, b, c)
        if not is_equivalent:
            all_equivalent = False
            print(f"Test case ({a}, {b}, {c}) failed equivalence check.")
            break
        else:
            print(f"Test case ({a}, {b}, {c}) passed equivalence check.")
    if all_equivalent:
        print("\nAll test cases passed the equivalence check.")
    else:
        print("\nSome test cases failed the equivalence check.")