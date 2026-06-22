import random

class ExpressionEvaluator:
    TEST_COUNT = 100

    @staticmethod
    def evaluate(a, b, c, d):
        return (a and b) or (c and not d)

    @staticmethod
    def run_verification():
        for _ in range(ExpressionEvaluator.TEST_COUNT):
            inputs = [random.choice([True, False]) for _ in range(4)]
            expected = ExpressionEvaluator.evaluate(*inputs)
            actual = (inputs[0] and inputs[1]) or (inputs[2] and not inputs[3])
            if expected != actual:
                raise AssertionError(f"Verification failed for {inputs}")
        return ExpressionEvaluator.TEST_COUNT

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    result = ExpressionEvaluator.evaluate(sample_a, sample_b, sample_c, sample_d)
    print(result)
    count = ExpressionEvaluator.run_verification()
    print(count)