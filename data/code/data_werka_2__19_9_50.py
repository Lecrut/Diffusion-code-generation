class ConditionEvaluator:
    @staticmethod
    def evaluate_condition(x, y):
        yield x > y

if __name__ == '__main__':
    sample_x = 15
    sample_y = 25
    evaluator = ConditionEvaluator()
    result_generator = evaluator.evaluate_condition(sample_x, sample_y)
    result = next(result_generator)
    print(result)