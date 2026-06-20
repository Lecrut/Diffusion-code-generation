class NumberEvaluator:
    def __init__(self, value):
        self.value = value

    def is_negative(self):
        return self.value < 0

if __name__ == '__main__':
    sample_number_1 = -15
    evaluator1 = NumberEvaluator(sample_number_1)
    print(f"The sample number is: {sample_number_1}")
    print(f"Is the sample number negative? {evaluator1.is_negative()}")

    sample_number_2 = 42
    evaluator2 = NumberEvaluator(sample_number_2)
    print(f"The sample number is: {sample_number_2}")
    print(f"Is the sample number negative? {evaluator2.is_negative()}")