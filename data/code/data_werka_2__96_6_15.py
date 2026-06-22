class BooleanLogicEvaluator:
    MASK_TRUE = 0xFFFFFFFFFFFFFFFF
    MASK_FALSE = 0

    @staticmethod
    def to_bit(val):
        return 1 if val else 0

    @staticmethod
    def evaluate_logic(A, B, C, D):
        a_bit = BooleanLogicEvaluator.to_bit(A)
        b_bit = BooleanLogicEvaluator.to_bit(B)
        c_bit = BooleanLogicEvaluator.to_bit(C)
        d_bit = BooleanLogicEvaluator.to_bit(D)

        term1 = a_bit & b_bit
        not_d_bit = 1 ^ d_bit
        term2 = c_bit & not_d_bit

        result = term1 | term2
        return result

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = BooleanLogicEvaluator.evaluate_logic(A, B, C, D)
    print(result)