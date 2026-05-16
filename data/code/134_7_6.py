def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] != conditions[j]:
                return True
    return False
if __name__ == '__main__':
    condition1 = lambda: True
    condition2 = lambda: False
    condition3 = lambda: True
    condition4 = lambda: False
    test_cases = [
        [condition1, condition2],
        [condition1, condition1],
        [condition2, condition2],
        [condition1, condition3],
        [condition2, condition4],
        [condition1, condition4],
        [condition1, condition2, condition3],
        [condition1, condition1, condition2]
    ]
    for i, conditions in enumerate(test_cases):
        result = check_mutual_exclusivity(conditions)
        print(f"Test Case {i+1}: {conditions}: Mutual Exclusivity Found: {result}")