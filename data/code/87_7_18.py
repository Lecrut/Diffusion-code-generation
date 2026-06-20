class BooleanCombiner:
    AND = 'and'
    OR = 'or'

    @staticmethod
    def combine_expression(expr1, expr2, operator):
        if operator == BooleanCombiner.AND:
            return expr1 and expr2
        elif operator == BooleanCombiner.OR:
            return expr1 or expr2
        else:
            raise ValueError('Invalid operator')

    @classmethod
    def combine_complex_expressions(cls, expr1, expr2, expr3, expr4, operator):
        if operator == cls.AND:
            return (expr1 and expr2) and (expr3 and expr4)
        elif operator == cls.OR:
            return (expr1 or expr2) or (expr3 or expr4)
        else:
            raise ValueError('Invalid operator')
if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = False
    result = BooleanCombiner.combine_expression(a, b, BooleanCombiner.AND)
    print(result)
    result = BooleanCombiner.combine_complex_expressions(a, b, c, d, BooleanCombiner.OR)
    print(result)