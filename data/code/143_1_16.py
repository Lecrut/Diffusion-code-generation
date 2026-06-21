def check_contradiction(expressions):
    contradictions = set()
    for expr1 in expressions:
        for expr2 in expressions:
            if expr1 != expr2:
                contradictions.add((expr1, expr2))
    return len(contradictions) > 0

if __name__ == '__main__':
    expressions1 = [True, False, True]
    print(f"Expressions: {expressions1}, Contradiction found: {check_contradiction(expressions1)}")
    expressions2 = [True, False]
    print(f"Expressions: {expressions2}, Contradiction found: {check_contradiction(expressions2)}")
    expressions3 = [True, True, True]
    print(f"Expressions: {expressions3}, Contradiction found: {check_contradiction(expressions3)}")