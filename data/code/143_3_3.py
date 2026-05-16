def check_contradictory_combination(bool_list):
    n = len(bool_list)
    for i in range(n):
        for j in range(i + 1, n):
            if bool_list[i] != bool_list[j]:
                return True
    return False
if __name__ == '__main__':
    test_cases = [
        [True, True, True],
        [False, False, False],
        [True, False, True],
        [True, True, False],
        [False, True, False],
        [True, False],
        [False, False]
    ]
    for case in test_cases:
        result = check_contradictory_combination(case)
        print(f"Input: {case}, Result: {result}")