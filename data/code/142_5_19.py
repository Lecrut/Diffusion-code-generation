class BooleanComparator:
    @staticmethod
    def compare_truth_values(value1: bool, value2: bool) -> bool:
        return value1 == value2

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = BooleanComparator.compare_truth_values(sample_a, sample_b)
    print(f"Sample A: {sample_a}, Sample B: {sample_b}, Comparison Result: {result}")