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
            pass
    return False
if __name__ == '__main__':
    expressions1 = [True, True, False]
    print(f"Expressions: {expressions1}, Contradiction found: {check_contradiction(expressions1)}")
    expressions2 = [True, False]
    print(f"Expressions: {expressions2}, Contradiction found: {check_contradiction(expressions2)}")
    expressions3 = [True, True, True]
    print(f"Expressions: {expressions3}, Contradiction found: {check_contradiction(expressions3)}")
    expressions4 = [True, False, True]
    print(f"Expressions: {expressions4}, Contradiction found: {check_contradiction(expressions4)}")