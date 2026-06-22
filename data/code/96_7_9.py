import random

class BooleanEvaluator:
    def __init__(self):
        self.results = []

    def evaluate(self, a, b, c, d):
        return (a and b) or (c and not d)

    def run_verification(self):
        for _ in range(100):
            a = random.choice([True, False])
            b = random.choice([True, False])
            c = random.choice([True, False])
            d = random.choice([True, False])
            expected = (a and b) or (c and not d)
            actual = self.evaluate(a, b, c, d)
            if actual != expected:
                raise AssertionError(f"Verification failed for a={a}, b={b}, c={c}, d={d}")
        return True

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    sample_result = evaluator.evaluate(sample_a, sample_b, sample_c, sample_d)
    print(sample_result)
    verification_passed = evaluator.run_verification()
    print(verification_passed)