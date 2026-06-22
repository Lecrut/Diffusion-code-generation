def check_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return a == False and b == False

class BooleanEvaluator:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def evaluate(self):
        return check_both_false(self.val1, self.val2)

if __name__ == '__main__':
    result1 = check_both_false(False, False)
    print(result1)
    
    evaluator = BooleanEvaluator(False, False)
    result2 = evaluator.evaluate()
    print(result2)
    
    evaluator2 = BooleanEvaluator(True, False)
    result3 = evaluator2.evaluate()
    print(result3)