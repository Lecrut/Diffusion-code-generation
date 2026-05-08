def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] != conditions[j]:
                return True
    return False
if __name__ == '__main__':
    cond1 = lambda: True
    cond2 = lambda: False
    cond3 = lambda: True
    conditions1 = [cond1, cond2, cond3]
    print(f"Conditions 1: {conditions1}")
    print(f"Mutually exclusive: {check_mutual_exclusivity(conditions1)}")
    cond4 = lambda: True
    cond5 = lambda: True
    cond6 = lambda: True
    conditions2 = [cond4, cond5, cond6]
    print(f"Conditions 2: {conditions2}")
    print(f"Mutually exclusive: {check_mutual_exclusivity(conditions2)}")
    cond7 = lambda: False
    cond8 = lambda: False
    cond9 = lambda: False
    conditions3 = [cond7, cond8, cond9]
    print(f"Conditions 3: {conditions3}")
    print(f"Mutually exclusive: {check_mutual_exclusivity(conditions3)}")
    cond10 = lambda: True
    cond11 = lambda: False
    conditions4 = [cond10, cond11]
    print(f"Conditions 4: {conditions4}")
    print(f"Mutually exclusive: {check_mutual_exclusivity(conditions4)}")
    conditions5 = [cond1]
    print(f"Conditions 5: {conditions5}")
    print(f"Mutually exclusive: {check_mutual_exclusivity(conditions5)}")
    conditions6 = []
    print(f"Conditions 6: {conditions6}")
    print(f"Mutually exclusive: {check_mutual_exclusivity(conditions6)}")