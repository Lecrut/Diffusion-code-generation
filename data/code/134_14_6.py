def check_mutual_exclusivity(constraints):
    if not constraints:
        return True
    n = len(constraints)
    constraint_set = set(constraints)
    for i in range(n):
        for j in range(i + 1, n):
            if constraints[i] == constraints[j]:
                return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [1, 2, 3, 4]
    print(f"Constraints: {sample_constraints_1}, Mutual Exclusivity: {check_mutual_exclusivity(sample_constraints_1)}")
    sample_constraints_2 = [1, 2, 1, 3]
    print(f"Constraints: {sample_constraints_2}, Mutual Exclusivity: {check_mutual_exclusivity(sample_constraints_2)}")
    sample_constraints_3 = [5, 6, 7, 8]
    print(f"Constraints: {sample_constraints_3}, Mutual Exclusivity: {check_mutual_exclusivity(sample_constraints_3)}")
    sample_constraints_4 = [10, 20, 10]
    print(f"Constraints: {sample_constraints_4}, Mutual Exclusivity: {check_mutual_exclusivity(sample_constraints_4)}")
    sample_constraints_5 = []
    print(f"Constraints: {sample_constraints_5}, Mutual Exclusivity: {check_mutual_exclusivity(sample_constraints_5)}")