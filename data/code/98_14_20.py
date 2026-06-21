class ConditionEvaluator:
    THRESHOLD_A = 0
    THRESHOLD_B = 10
    EQUALITY_C = 5

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def _check_first_pair(self):
        return self.a > self.THRESHOLD_A and self.b < self.THRESHOLD_B

    def _check_second_pair(self):
        return self.c == self.EQUALITY_C and self.d is not None

    def evaluate(self):
        first_part = self._check_first_pair()
        second_part = self._check_second_pair()
        return first_part or second_part

if __name__ == '__main__':
    evaluator = ConditionEvaluator(
        a=15,
        b=5,
        c=5,
        d="exists"
    )
    result = evaluator.evaluate()
    print(result)