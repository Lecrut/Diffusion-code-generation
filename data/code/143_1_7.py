import itertools
def check_contradiction(expressions):
    n = len(expressions)
    for i in range(n):
        for j in range(i + 1, n):
            expr1 = expressions[i]
            expr2 = expressions[j]
            if expr1 and not expr2:
                return True
            if expr2 and not expr1:
                return True
    return False
if __name__ == '__main__':
    sample1 = [True, True, False]
    print(f"Sample 1: {check_contradiction(sample1)}")
    sample2 = [True, False]
    print(f"Sample 2: {check_contradiction(sample2)}")
    sample3 = [True, True, True]
    print(f"Sample 3: {check_contradiction(sample3)}")
    sample4 = [True, False, True]
    print(f"Sample 4: {check_contradiction(sample4)}")
    sample5 = [False, False]
    print(f"Sample 5: {check_contradiction(sample5)}")
    sample6 = [True, True, False, True]
    print(f"Sample 6: {check_contradiction(sample6)}")
    sample7 = [True, False, True, False]
    print(f"Sample 7: {check_contradiction(sample7)}")