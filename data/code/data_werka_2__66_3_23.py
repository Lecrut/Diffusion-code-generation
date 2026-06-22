class AdjacentPairEvaluator:
    @staticmethod
    def evaluate_pairs(lst):
        if not all(isinstance(x, (int, float)) for x in lst):
            raise ValueError("All elements must be numbers")
        if len(lst) < 2:
            return []
        return [lst[i] < lst[i + 1] for i in range(len(lst) - 1)]

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7]
    sample_input_2 = [10, 20, 20, 30]
    sample_input_3 = [5, 5, 5]
    sample_input_4 = [1, 2, 1]

    evaluator = AdjacentPairEvaluator()
    
    print(evaluator.evaluate_pairs(sample_input_1))
    print(evaluator.evaluate_pairs(sample_input_2))
    print(evaluator.evaluate_pairs(sample_input_3))
    print(evaluator.evaluate_pairs(sample_input_4))