class TruthyEvaluator:
    @staticmethod
    def has_truthy_value(iterable):
        return any(iterable)

if __name__ == '__main__':
    sample_values = [0, False, None, [], {}, (), '']
    evaluator = TruthyEvaluator()
    result = evaluator.has_truthy_value(sample_values)
    print(result)