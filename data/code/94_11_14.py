class BooleanEvaluator:
    def __init__(self, initial_value):
        self.initial_value = initial_value

    def is_any_true(self, bool_list):
        return self.initial_value or any(bool_list)

if __name__ == '__main__':
    evaluator1 = BooleanEvaluator(True)
    print(f"Result 1: {evaluator1.is_any_true([False, False])}")
    
    evaluator2 = BooleanEvaluator(False)
    print(f"Result 2: {evaluator2.is_any_true([True, False])}")
    
    evaluator3 = BooleanEvaluator(False)
    print(f"Result 3: {evaluator3.is_any_true([False, True])}")
    
    evaluator4 = BooleanEvaluator(False)
    print(f"Result 4: {evaluator4.is_any_true([])}")