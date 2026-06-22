class BooleanEvaluator:
    def __init__(self, initial_value, values):
        self.initial_value = initial_value
        self.values = values

    def check_any_true(self):
        if self.initial_value:
            return True
        for val in self.values:
            if val:
                return True
        return False

    def get_initial(self):
        return self.initial_value

    def get_values(self):
        return self.values

if __name__ == '__main__':
    evaluator = BooleanEvaluator(False, [False, True, False])
    result1 = evaluator.check_any_true()
    print(result1)
    
    evaluator2 = BooleanEvaluator(True, [False, False])
    result2 = evaluator2.check_any_true()
    print(result2)
    
    evaluator3 = BooleanEvaluator(False, [])
    result3 = evaluator3.check_any_true()
    print(result3)