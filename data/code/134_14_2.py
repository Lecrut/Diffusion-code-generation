import itertools
def check_mutual_exclusivity(constraints):
    if not constraints:
        return True
    n = len(constraints)
    if n <= 1:
        return True
    for i in range(n):
        for j in range(i + 1, n):
            if constraints[i] == constraints[j]:
                return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [1, 2, 3, 4]
    print(check_mutual_exclusivity(sample_constraints_1))
    sample_constraints_2 = [1, 2, 3, 1]
    print(check_mutual_exclusivity(sample_constraints_2))
    sample_constraints_3 = [5, 6, 7, 8]
    print(check_mutual_exclusivity(sample_constraints_3))
    sample_constraints_4 = [10, 20, 30, 10]
    print(check_mutual_exclusivity(sample_constraints_4))
    sample_constraints_5 = []
    print(check_mutual_exclusivity(sample_constraints_5))
    sample_constraints_6 = [42]
    print(check_mutual_exclusivity(sample_constraints_6))