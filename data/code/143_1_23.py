def check_contradiction(expressions):
    if not all(isinstance(expr, bool) for expr in expressions):
        raise ValueError("All elements in the list must be boolean values.")
    
    true_set = set(index for index, expr in enumerate(expressions) if expr)
    false_set = set(index for index, expr in enumerate(expressions) if not expr)
    
    return true_set.intersection(false_set)

if __name__ == '__main__':
    expressions1 = [True, False, True]
    print(f"Expressions: {expressions1}, Contradiction found: {check_contradiction(expressions1)}")
    expressions2 = [True, False]
    print(f"Expressions: {expressions2}, Contradiction found: {check_contradiction(expressions2)}")
    expressions3 = [True, True, True]
    print(f"Expressions: {expressions3}, Contradiction found: {check_contradiction(expressions3)}")
    expressions4 = [True, False, True, False]
    print(f"Expressions: {expressions4}, Contradiction found: {check_contradiction(expressions4)}")