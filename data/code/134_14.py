def check_mutual_exclusivity(constraints):
    if not constraints:
        return True
    n = len(constraints)
    indices = set(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if constraints[i] == constraints[j]:
                return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [1, 2, 3]
    result_1 = check_mutual_exclusivity(sample_constraints_1)
    print(f"Constraints: {sample_constraints_1}, Mutual Exclusivity: {result_1}")
    sample_constraints_2 = [1, 2, 1]
    result_2 = check_mutual_exclusivity(sample_constraints_2)
    print(f"Constraints: {sample_constraints_2}, Mutual Exclusivity: {result_2}")
    sample_constraints_3 = [5, 8, 10]
    result_3 = check_mutual_exclusivity(sample_constraints_3)
    print(f"Constraints: {sample_constraints_3}, Mutual Exclusivity: {result_3}")
    sample_constraints_4 = []
    result_4 = check_mutual_exclusivity(sample_constraints_4)
    print(f"Constraints: {sample_constraints_4}, Mutual Exclusivity: {result_4}")
    sample_constraints_5 = [7, 7, 7, 7]
    result_5 = check_mutual_exclusivity(sample_constraints_5)
    print(f"Constraints: {sample_constraints_5}, Mutual Exclusivity: {result_5}")