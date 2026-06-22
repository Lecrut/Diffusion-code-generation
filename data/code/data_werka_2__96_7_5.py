import random
import math

class BooleanExpressionEvaluator:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self):
        left_and = self.a and self.b
        not_d = not self.d
        right_and = self.c and not_d
        return left_and or right_and

    def get_values(self):
        return self.a, self.b, self.c, self.d

def run_verification():
    for _ in range(100):
        r_a = random.choice([True, False])
        r_b = random.choice([True, False])
        r_c = random.choice([True, False])
        r_d = random.choice([True, False])
        instance = BooleanExpressionEvaluator(r_a, r_b, r_c, r_d)
        result = instance.evaluate()
        expected = (r_a and r_b) or (r_c and not r_d)
        if result != expected:
            raise AssertionError(f"Mismatch for {r_a}, {r_b}, {r_c}, {r_d}")
    return True

if __name__ == '__main__':
    instance = BooleanExpressionEvaluator(True, False, True, False)
    print(instance.evaluate())
    print(instance.get_values())
    run_verification()