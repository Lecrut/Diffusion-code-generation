class BooleanExpressionEvaluator:
    TRUE_VAL = True
    FALSE_VAL = False
    NOT_MAP = {TRUE_VAL: FALSE_VAL, FALSE_VAL: TRUE_VAL}

    @staticmethod
    def apply_not(value):
        return BooleanExpressionEvaluator.NOT_MAP[value]

    @staticmethod
    def evaluate():
        a = True
        b = False
        c = True
        d = False
        
        p1 = a and b or c
        p2 = (a and b) or c
        p3 = a and (b or c)
        p4 = not a and b or c
        p5 = not (a and b) or c
        p6 = a or b and c
        p7 = (a or b) and c
        p8 = not a or b and c
        p9 = not (a or b) and c
        p10 = a and not b or c
        
        results = {
            "a and b or c": p1,
            "(a and b) or c": p2,
            "a and (b or c)": p3,
            "not a and b or c": p4,
            "not (a and b) or c": p5,
            "a or b and c": p6,
            "(a or b) and c": p7,
            "not a or b and c": p8,
            "not (a or b) and c": p9,
            "a and not b or c": p10
        }
        return results

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    output = evaluator.evaluate()
    print(output)