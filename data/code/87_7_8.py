class BooleanCombiner:
    TRUE = True
    FALSE = False

    @staticmethod
    def combine(expr1, expr2):
        return (expr1 and not expr2) or (not expr1 and expr2)

if __name__ == '__main__':
    sample_expr1 = BooleanCombiner.TRUE
    sample_expr2 = BooleanCombiner.FALSE
    result = BooleanCombiner.combine(sample_expr1, sample_expr2)
    print(result)