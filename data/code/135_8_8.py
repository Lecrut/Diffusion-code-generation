def check_equivalence(test_cases):
    result1 = {}
    result2 = {}
    for case in test_cases:
        result1[case] = (case % 2 == 0)
        result2[case] = (case % 2 == 0)
    is_equivalent = True
    for case in test_cases:
        if result1[case] != result2[case]:
            is_equivalent = False
            break
    return is_equivalent, result1, result2
if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def structure_a(n):
        return "Even" if n % 2 == 0 else "Odd"
    def structure_b(n):
        return "Even" if n % 2 == 0 else "Odd"
    equivalence, res_a, res_b = check_equivalence(test_data)
    print(f"Test Cases: {test_data}")
    print("-" * 30)
    print("Results from Structure A:")
    for t, r in res_a.items():
        print(f"Input {t}: {r}")
    print("-" * 30)
    print("Results from Structure B:")
    for t, r in res_b.items():
        print(f"Input {t}: {r}")
    print("-" * 30)
    print(f"Are the results of Structure A and Structure B equivalent? {equivalence}")