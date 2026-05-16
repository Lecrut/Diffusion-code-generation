def check_equivalence(a, b, c):
    return (a == b) == (c == b)
def check_equivalence_logic(a, b, c):
    return (a == b) and (c == b)
if __name__ == '__main__':
    test_cases = [
        (1, 2, 2),
        (3, 4, 4),
        (5, 6, 6),
        (1, 3, 2),
        (1, 2, 3)
    ]
    print("--- Equivalence Check using (a == b) == (c == b) ---")
    for a, b, c in test_cases:
        result = check_equivalence(a, b, c)
        print(f"Test Case ({a}, {b}, {c}): Result = {result}")
    print("\n--- Equivalence Check using (a == b) and (c == b) ---")
    for a, b, c in test_cases:
        result = check_equivalence_logic(a, b, c)
        print(f"Test Case ({a}, {b}, {c}): Result = {result}")