class LogicEvaluator:
    OP_AND = "and"
    OP_OR = "or"
    OP_NOT = "not"

    @staticmethod
    def evaluate_not(val):
        return not val

    @staticmethod
    def evaluate_or(left, right):
        return left or right

    @staticmethod
    def evaluate_and(left, right):
        return left and right

    @classmethod
    def check_logic(cls, A, B, C):
        not_c = cls.evaluate_not(C)
        b_or_not_c = cls.evaluate_or(B, not_c)
        result = cls.evaluate_and(A, b_or_not_c)
        return result

if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = LogicEvaluator.check_logic(A_val, B_val, C_val)
    print(result)