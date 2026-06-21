def validate_bitwise_integers(A, B, C, D):
    for val in (A, B, C, D):
        if not isinstance(val, int):
            raise ValueError("Inputs must be integers")
        if val not in (0, 1):
            raise ValueError("Inputs must be 0 or 1 for bitwise logic")
    return A, B, C, D

def evaluate_logic_bitwise(A, B, C, D):
    valid_A, valid_B, valid_C, valid_D = validate_bitwise_integers(A, B, C, D)
    term1 = valid_A & valid_B
    term2 = valid_C & (1 - valid_D)
    result = term1 | term2
    return result

class LogicEvaluator:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def compute(self):
        return evaluate_logic_bitwise(self.A, self.B, self.C, self.D)

if __name__ == '__main__':
    evaluator = LogicEvaluator(1, 0, 1, 0)
    result = evaluator.compute()
    print(result)