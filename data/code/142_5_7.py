class BooleanComparator:
    @staticmethod
    def check_truth_value_match(value1: bool, value2: bool) -> bool:
        return value1 == value2

if __name__ == '__main__':
    comparator = BooleanComparator()
    sample_a = True
    sample_b = False
    result_a = comparator.check_truth_value_match(sample_a, True)
    result_b = comparator.check_truth_value_match(sample_b, False)
    print(f"Sample A: {sample_a}, Result A: {result_a}")
    print(f"Sample B: {sample_b}, Result B: {result_b}")