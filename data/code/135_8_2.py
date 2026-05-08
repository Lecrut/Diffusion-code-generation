def check_equivalence(test_cases):
    result1 = {}
    result2 = {}
    for case in test_cases:
        result1[case] = (case % 2 == 0)
        result2[case] = (case // 2) % 3
    is_equivalent = True
    for case in test_cases:
        if result1[case] != result2[case]:
            is_equivalent = False
            break
    return is_equivalent, result1, result2
if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def structure_a(data):
        output = {}
        for x in data:
            output[x] = x % 2 == 0
        return output
    def structure_b(data):
        output = {}
        for x in data:
            output[x] = (x // 2) % 3
        return output
    output_a = structure_a(test_data)
    output_b = structure_b(test_data)
    print("Test Data:", test_data)
    print("\nOutput of Structure A (x % 2 == 0):", output_a)
    print("Output of Structure B ((x // 2) % 3):", output_b)
    equivalence_check = check_equivalence(test_data)
    is_eq, res1, res2 = equivalence_check
    print("\nEquivalence Check Result:")
    print(f"Are the outputs equivalent? {is_eq}")
    print("Result A:", res1)
    print("Result B:", res2)