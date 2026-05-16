import itertools
def check_conditional_identity(code1, code2):
    test_cases = [
        (0, 1),
        (1, 0),
        (0, 0),
        (1, 1)
    ]
    def evaluate(code, a, b):
        try:
            exec(code, {'True': True, 'False': False, 'if': lambda c: c})
            return eval(code, {'True': True, 'False': False, 'if': lambda c: c}, {'a': a, 'b': b})
        except Exception:
            return None
    results1 = set()
    results2 = set()
    for a, b in test_cases:
        try:
            res1 = evaluate(code1, a, b)
            if res1 is not None:
                results1.add(tuple(sorted(res1)))
        except Exception:
            pass
        try:
            res2 = evaluate(code2, a, b)
            if res2 is not None:
                results2.add(tuple(sorted(res2)))
        except Exception:
            pass
    return results1 == results2
if __name__ == '__main__':
    code_a = "if a > b: result = 1 else: result = 0"
    code_b = "if a >= b: result = 1 else: result = 0"
    result = check_conditional_identity(code_a, code_b)
    print(result)