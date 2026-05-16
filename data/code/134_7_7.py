def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] != conditions[j]:
                return True
    return False
if __name__ == '__main__':
    conditions1 = [lambda: True, lambda: False]
    conditions2 = [lambda: True, lambda: True]
    conditions3 = [lambda: False, lambda: False]
    conditions4 = [lambda: True, lambda: False, lambda: True]
    conditions5 = [lambda: True, lambda: True, lambda: False]
    conditions6 = [lambda: True, lambda: True, lambda: True]
    conditions7 = [lambda: False, lambda: False, lambda: False]
    print(f"Conditions1: {check_mutual_exclusivity(conditions1)}")
    print(f"Conditions2: {check_mutual_exclusivity(conditions2)}")
    print(f"Conditions3: {check_mutual_exclusivity(conditions3)}")
    print(f"Conditions4: {check_mutual_exclusivity(conditions4)}")
    print(f"Conditions5: {check_mutual_exclusivity(conditions5)}")
    print(f"Conditions6: {check_mutual_exclusivity(conditions6)}")
    print(f"Conditions7: {check_mutual_exclusivity(conditions7)}")