import itertools
def check_contradiction(expressions):
    n = len(expressions)
    for i in range(n):
        for j in range(i + 1, n):
            expr1 = expressions[i]
            expr2 = expressions[j]
            if expr1 and not expr2 and expr2 and not expr1:
                return True
    return False
if __name__ == '__main__':
    expressions1 = [True, False, True]
    print(f"Expressions: {expressions1}, Contradiction found: {check_contradiction(expressions1)}")
    expressions2 = [True, False]
    print(f"Expressions: {expressions2}, Contradiction found: {check_contradiction(expressions2)}")
    expressions3 = [True, True, False]
    print(f"Expressions: {expressions3}, Contradiction found: {check_contradiction(expressions3)}")
    expressions4 = [True, False, True, False]
    print(f"Expressions: {expressions4}, Contradiction found: {check_contradiction(expressions4)}")
    expressions5 = [True, True]
    print(f"Expressions: {expressions5}, Contradiction found: {check_contradiction(expressions5)}")
    expressions6 = [True, False]
    print(f"Expressions: {expressions6}, Contradiction found: {check_contradiction(expressions6)}")
    expressions7 = [True, True, False]
    print(f"Expressions: {expressions7}, Contradiction found: {check_contradiction(expressions7)}")