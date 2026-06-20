class TruthEvaluator:
    TRUE_STRING = 'True'
    FALSE_STRING = 'False'

    @staticmethod
    def evaluate_truth_values(bool_list):
        return [TruthEvaluator.TRUE_STRING if b else TruthEvaluator.FALSE_STRING for b in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    evaluator = TruthEvaluator()
    print(evaluator.evaluate_truth_values(sample_values))