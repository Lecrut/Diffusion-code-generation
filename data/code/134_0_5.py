def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] and conditions[j]:
                return False
    return True
if __name__ == '__main__':
    sample1 = [(True, False), (False, True)]
    print(f"Sample 1: {check_mutual_exclusivity(sample1)}")
    sample2 = [(True, True), (False, False)]
    print(f"Sample 2: {check_mutual_exclusivity(sample2)}")
    sample3 = [(True, False), (False, True), (True, True)]
    print(f"Sample 3: {check_mutual_exclusivity(sample3)}")
    sample4 = [(True, False), (False, True), (False, False)]
    print(f"Sample 4: {check_mutual_exclusivity(sample4)}")
    sample5 = [(True, True), (False, False), (True, False)]
    print(f"Sample 5: {check_mutual_exclusivity(sample5)}")