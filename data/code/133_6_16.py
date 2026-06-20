class FlagEvaluator:
    def __init__(self, flag_list):
        self.flag_list = flag_list

    @staticmethod
    def convert_to_booleans(flag_list):
        return [bool(flag) for flag in flag_list]

    @staticmethod
    def evaluate_consistency(booleans):
        return all(booleans)

    def process_flags(self):
        booleans = self.convert_to_booleans(self.flag_list)
        is_consistent = self.evaluate_consistency(booleans)
        return booleans, is_consistent

if __name__ == '__main__':
    sample_flags = [1, 0, 1, 1, 0]
    evaluator = FlagEvaluator(sample_flags)
    result_booleans, result_consistency = evaluator.process_flags()
    print("Booleans:", result_booleans)
    print("Consistency:", result_consistency)