class TruthTableValidator:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def evaluate_expression(p, q):
        return (p and q) or (not p and not q)

    @classmethod
    def validate_truth_table(cls):
        values = [cls.TRUE, cls.FALSE]
        for p in values:
            for q in values:
                result = cls.evaluate_expression(p, q)
                if result != cls.TRUE:
                    return False
        return True

if __name__ == '__main__':
    print(TruthTableValidator.validate_truth_table())