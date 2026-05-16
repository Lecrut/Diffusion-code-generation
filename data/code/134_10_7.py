def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if any(conditions[i][k] and conditions[j][k] for k in range(len(conditions[i]))):
                return False
    return True
if __name__ == '__main__':
    sample_conditions_1 = [
        [True, False],
        [False, True],
        [True, True]
    ]
    result_1 = check_mutual_exclusivity(sample_conditions_1)
    print(f"Sample 1 Result: {result_1}")
    sample_conditions_2 = [
        [True],
        [False],
        [True]
    ]
    result_2 = check_mutual_exclusivity(sample_conditions_2)
    print(f"Sample 2 Result: {result_2}")
    sample_conditions_3 = [
        [True, True],
        [True, False]
    ]
    result_3 = check_mutual_exclusivity(sample_conditions_3)
    print(f"Sample 3 Result: {result_3}")
    sample_conditions_4 = [
        [True, True],
        [True, True]
    ]
    result_4 = check_mutual_exclusivity(sample_conditions_4)
    print(f"Sample 4 Result: {result_4}")
    sample_conditions_5 = [
        [True, False],
        [False, True]
    ]
    result_5 = check_mutual_exclusivity(sample_conditions_5)
    print(f"Sample 5 Result: {result_5}")