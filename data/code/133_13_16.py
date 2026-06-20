class TruthEvaluator:
    TRUE_STR = 'True'
    FALSE_STR = 'False'

    @staticmethod
    def evaluate_truth_values(bool_list):
        return [TruthEvaluator.TRUE_STR if b else TruthEvaluator.FALSE_STR for b in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(TruthEvaluator.evaluate_truth_values(sample_values))