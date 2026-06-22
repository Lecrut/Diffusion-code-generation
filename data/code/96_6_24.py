class BitwiseLogicEvaluator:
    MASK = 1

    def __init__(self, a_val, b_val, c_val, d_val):
        self.a = a_val
        self.b = b_val
        self.c = c_val
        self.d = d_val

    def to_bit(self, val):
        return 1 if val else 0

    def evaluate(self):
        ab = (self.to_bit(self.a) & self.to_bit(self.b)) << 1
        cd = (self.to_bit(self.c) & (1 - self.to_bit(self.d)))
        combined = ab | cd
        return combined & 1

    def get_raw_bits(self):
        a_bit = self.to_bit(self.a)
        b_bit = self.to_bit(self.b)
        c_bit = self.to_bit(self.c)
        d_bit = self.to_bit(self.d)
        not_d = 1 - d_bit
        term1 = a_bit & b_bit
        term2 = c_bit & not_d
        return term1, term2

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    evaluator = BitwiseLogicEvaluator(A, B, C, D)
    result = evaluator.evaluate()
    term1, term2 = evaluator.get_raw_bits()
    print(result)
    print(term1)
    print(term2)