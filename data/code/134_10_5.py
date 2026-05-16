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
        [False, True]
    ]
    print(f"Sample 1: {check_mutual_exclusivity(sample_conditions_1)}")
    sample_conditions_2 = [
        [True],
        [True]
    ]
    print(f"Sample 2: {check_mutual_exclusivity(sample_conditions_2)}")
    sample_conditions_3 = [
        [True, False],
        [False, True],
        [True, True]
    ]
    print(f"Sample 3: {check_mutual_exclusivity(sample_conditions_3)}")
    sample_conditions_4 = [
        [True, True],
        [True, True]
    ]
    print(f"Sample 4: {check_mutual_exclusivity(sample_conditions_4)}")
    sample_conditions_5 = [
        [True, False],
        [False, True],
        [True, False]
    ]
    print(f"Sample 5: {check_mutual_exclusivity(sample_conditions_5)}")