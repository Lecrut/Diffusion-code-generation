def check_mutual_exclusivity(constraints):
    if not constraints:
        return True
    n = len(constraints)
    indices = list(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if constraints[i] and constraints[j]:
                return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [True, False, True, False]
    result_1 = check_mutual_exclusivity(sample_constraints_1)
    print(f"Constraints: {sample_constraints_1}")
    print(f"Mutual Exclusivity: {result_1}")
    sample_constraints_2 = [True, True, False, True]
    result_2 = check_mutual_exclusivity(sample_constraints_2)
    print(f"Constraints: {sample_constraints_2}")
    print(f"Mutual Exclusivity: {result_2}")
    sample_constraints_3 = [False, False, False]
    result_3 = check_mutual_exclusivity(sample_constraints_3)
    print(f"Constraints: {sample_constraints_3}")
    print(f"Mutual Exclusivity: {result_3}")
    sample_constraints_4 = [True, True, True]
    result_4 = check_mutual_exclusivity(sample_constraints_4)
    print(f"Constraints: {sample_constraints_4}")
    print(f"Mutual Exclusivity: {result_4}")
    sample_constraints_5 = []
    result_5 = check_mutual_exclusivity(sample_constraints_5)
    print(f"Constraints: {sample_constraints_5}")
    print(f"Mutual Exclusivity: {result_5}")