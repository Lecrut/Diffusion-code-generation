class TruthEvaluator:
    def evaluate_truth_values(self, bool_list):
        return ['True' if b else 'False' for b in bool_list]

if __name__ == '__main__':
    evaluator = TruthEvaluator()
    sample_values = [True, False, True, False]
    print(evaluator.evaluate_truth_values(sample_values))