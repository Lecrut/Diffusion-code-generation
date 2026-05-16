import itertools
def check_contradiction(expressions):
    n = len(expressions)
    for i in range(n):
        for j in range(i + 1, n):
            expr1 = expressions[i]
            expr2 = expressions[j]
            if expr1 and not expr2 and expr2 and not expr1:
                return True
            if (expr1 and not expr2) or (not expr1 and expr2):
                pass
            if (expr1 and not expr2) or (not expr1 and expr2):
                return True
    return False
if __name__ == '__main__':
    expressions1 = [True, True, True]
    print(f"Test 1: {check_contradiction(expressions1)}")
    expressions2 = [True, False, True]
    print(f"Test 2: {check_contradiction(expressions2)}")
    expressions3 = [True, False]
    print(f"Test 3: {check_contradiction(expressions3)}")
    expressions4 = [True, True, False, False]
    print(f"Test 4: {check_contradiction(expressions4)}")
    expressions5 = []
    print(f"Test 5: {check_contradiction(expressions5)}")
    expressions6 = [True]
    print(f"Test 6: {check_contradiction(expressions6)}")