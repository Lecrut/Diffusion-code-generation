class LogicEvaluator:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def evaluate(self):
        inner_or = self.B or (not self.C)
        result = self.A and inner_or
        return result

def check_logic(A, B, C):
    evaluator = LogicEvaluator(A, B, C)
    return evaluator.evaluate()

if __name__ == '__main__':
    evaluator1 = LogicEvaluator(True, False, True)
    print(evaluator1.evaluate())
    
    evaluator2 = LogicEvaluator(True, True, False)
    print(evaluator2.evaluate())
    
    print(check_logic(False, True, False))