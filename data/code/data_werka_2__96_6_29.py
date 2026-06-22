class BitwiseLogicEvaluator:
    MASK = 1

    @staticmethod
    def to_bit(val):
        return val & BitwiseLogicEvaluator.MASK

    @staticmethod
    def evaluate(A, B, C, D):
        a = BitwiseLogicEvaluator.to_bit(A)
        b = BitwiseLogicEvaluator.to_bit(B)
        c = BitwiseLogicEvaluator.to_bit(C)
        d = BitwiseLogicEvaluator.to_bit(D)
        term1 = a & b
        not_d = d ^ BitwiseLogicEvaluator.MASK
        term2 = c & not_d
        result = term1 | term2
        return result

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    evaluator = BitwiseLogicEvaluator()
    result = evaluator.evaluate(A, B, C, D)
    print(result)