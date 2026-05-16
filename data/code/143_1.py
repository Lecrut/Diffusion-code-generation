import itertools
def check_contradiction(expressions):
    n = len(expressions)
    for i in range(n):
        for j in range(i + 1, n):
            expr1 = expressions[i]
            expr2 = expressions[j]
            if expr1 != (not expr2):
                continue
            if not (expr1 and expr2):
                pass
            if expr1 == (not expr2):
                return True
    return False
if __name__ == '__main__':
    expressions1 = [True, False, True]
    print(f"Expressions: {expressions1}, Contradiction: {check_contradiction(expressions1)}")
    expressions2 = [True, False]
    print(f"Expressions: {expressions2}, Contradiction: {check_contradiction(expressions2)}")
    expressions3 = [True, False]
    print(f"Expressions: {expressions3}, Contradiction: {check_contradiction(expressions3)}")
    expressions4 = [True, True]
    print(f"Expressions: {expressions4}, Contradiction: {check_contradiction(expressions4)}")
    expressions5 = [True, True, False]
    print(f"Expressions: {expressions5}, Contradiction: {check_contradiction(expressions5)}")
    expressions6 = [True, False]
    print(f"Expressions: {expressions6}, Contradiction: {check_contradiction(expressions6)}")
    expressions7 = [False, True]
    print(f"Expressions: {expressions7}, Contradiction: {check_contradiction(expressions7)}")
    expressions8 = [True, True, False, True]
    print(f"Expressions: {expressions8}, Contradiction: {check_contradiction(expressions8)}")