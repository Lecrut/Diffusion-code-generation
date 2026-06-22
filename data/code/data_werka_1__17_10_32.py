class NumberEvaluator:
    def __init__(self, value):
        self.value = value
    
    def is_even(self):
        return self.value % 2 == 0

if __name__ == '__main__':
    evaluator = NumberEvaluator(18)
    print(evaluator.is_even())
    evaluator.value = 3
    print(evaluator.is_even())