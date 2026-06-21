def check_contradiction(expressions):
    TRUE = True
    FALSE = False
    COND_TRUE_FALSE = (TRUE, FALSE)
    COND_FALSE_TRUE = (FALSE, TRUE)
    
    pairs = set(itertools.combinations(expressions, 2))
    for expr1, expr2 in pairs:
        if (expr1 == TRUE and expr2 == FALSE) or (expr1 == FALSE and expr2 == TRUE):
            return True
    return False

if __name__ == '__main__':
    expressions1 = [True, False, True]
    print(f"Expressions: {expressions1}, Contradiction: {check_contradiction(expressions1)}")
    
    expressions2 = [True, False]
    print(f"Expressions: {expressions2}, Contradiction: {check_contradiction(expressions2)}")
    
    expressions3 = [True, True, True]
    print(f"Expressions: {expressions3}, Contradiction: {check_contradiction(expressions3)}")