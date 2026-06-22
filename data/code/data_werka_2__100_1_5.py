def check_logic(A, B, C):
    return bool(A and (B or not C))

if __name__ == '__main__':
    class LogicEvaluator:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def evaluate(self):
            return check_logic(self.a, self.b, self.c)

    evaluator1 = LogicEvaluator(True, False, True)
    evaluator2 = LogicEvaluator(False, True, False)

    print(evaluator1.evaluate())
    print(evaluator2.evaluate())