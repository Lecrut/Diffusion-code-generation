class BitwiseLogicEvaluator:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def _to_bit(self, val):
        return 1 if val else 0

    def evaluate(self):
        a = self._to_bit(self.A)
        b = self._to_bit(self.B)
        c = self._to_bit(self.C)
        d = self._to_bit(self.D)
        
        term1 = a & b
        not_d = 1 ^ d
        term2 = c & not_d
        result = term1 | term2
        return result

if __name__ == '__main__':
    evaluator = BitwiseLogicEvaluator(1, 0, 1, 0)
    print(evaluator.evaluate())
    print(evaluator._to_bit(1))
    print(evaluator._to_bit(0))