import itertools
def check_mutual_exclusivity(constraints):
    if not constraints:
        return True
    n = len(constraints)
    for i in range(n):
        for j in range(i + 1, n):
            if constraints[i] == constraints[j]:
                return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [1, 2, 3]
    print(f"Constraints {sample_constraints_1}: {check_mutual_exclusivity(sample_constraints_1)}")
    sample_constraints_2 = [1, 2, 1]
    print(f"Constraints {sample_constraints_2}: {check_mutual_exclusivity(sample_constraints_2)}")
    sample_constraints_3 = [5, 8, 12]
    print(f"Constraints {sample_constraints_3}: {check_mutual_exclusivity(sample_constraints_3)}")
    sample_constraints_4 = [10, 10, 10, 5]
    print(f"Constraints {sample_constraints_4}: {check_mutual_exclusivity(sample_constraints_4)}")
    sample_constraints_5 = []
    print(f"Constraints {sample_constraints_5}: {check_mutual_exclusivity(sample_constraints_5)}")