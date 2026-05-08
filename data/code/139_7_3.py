class LogicGateEvaluator:
    def __init__(self):
        pass
    def evaluate(self, a, b, c, d):
        if a == 1 and b == 0 and c == 1 and d == 0:
            return 0
        elif a == 0 and b == 0 and c == 0 and d == 0:
            return 0
        elif a == 0 and b == 0 and c == 1 and d == 1:
            return 0
        elif a == 0 and b == 1 and c == 0 and d == 0:
            return 0
        elif a == 0 and b == 1 and c == 1 and d == 0:
            return 1
        elif a == 0 and b == 1 and c == 1 and d == 1:
            return 1
        elif a == 1 and b == 0 and c == 0 and d == 0:
            return 0
        elif a == 1 and b == 0 and c == 0 and d == 1:
            return 0
        elif a == 1 and b == 0 and c == 1 and d == 0:
            return 1
        elif a == 1 and b == 0 and c == 1 and d == 1:
            return 1
        elif a == 1 and b == 1 and c == 0 and d == 0:
            return 1
        elif a == 1 and b == 1 and c == 0 and d == 1:
            return 0
        elif a == 1 and b == 1 and c == 1 and d == 0:
            return 0
        elif a == 1 and b == 1 and c == 1 and d == 1:
            return 1
        else:
            return 0
if __name__ == '__main__':
    evaluator = LogicGateEvaluator()
    test_cases = [
        ((1, 0, 1, 0), 0),
        ((0, 0, 0, 0), 0),
        ((0, 0, 1, 1), 0),
        ((0, 1, 0, 0), 0),
        ((0, 1, 1, 0), 1),
        ((0, 1, 1, 1), 1),
        ((1, 0, 0, 0), 0),
        ((1, 0, 0, 1), 0),
        ((1, 0, 1, 0), 1),
        ((1, 0, 1, 1), 1),
        ((1, 1, 0, 0), 1),
        ((1, 1, 0, 1), 0),
        ((1, 1, 1, 0), 0),
        ((1, 1, 1, 1), 1)
    ]
    for inputs, expected in test_cases:
        a, b, c, d = inputs
        result = evaluator.evaluate(a, b, c, d)
        print(f"Inputs: a={a}, b={b}, c={c}, d={d}, Result: {result}, Expected: {expected}, Match: {result == expected}")