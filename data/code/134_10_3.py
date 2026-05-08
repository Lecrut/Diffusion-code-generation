def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if any(conditions[i][k] and conditions[j][k] for k in range(len(conditions[i]))):
                return False
    return True
if __name__ == '__main__':
    sample_conditions = [
        [True, False],
        [False, True],
        [True, True]
    ]
    result1 = check_mutual_exclusivity(sample_conditions)
    print(f"Result 1: {result1}")
    sample_conditions_2 = [
        [True],
        [False],
        [True]
    ]
    result2 = check_mutual_exclusivity(sample_conditions_2)
    print(f"Result 2: {result2}")
    sample_conditions_3 = [
        [True, True],
        [True, False]
    ]
    result3 = check_mutual_exclusivity(sample_conditions_3)
    print(f"Result 3: {result3}")
    sample_conditions_4 = [
        [True, False],
        [True, False]
    ]
    result4 = check_mutual_exclusivity(sample_conditions_4)
    print(f"Result 4: {result4}")
    sample_conditions_5 = [
        [True, True],
        [True, True]
    ]
    result5 = check_mutual_exclusivity(sample_conditions_5)
    print(f"Result 5: {result5}")