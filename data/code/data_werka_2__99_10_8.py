class BooleanExpressionEvaluator:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self):
        term1 = self.a and self.b
        term2 = term1 or self.c
        expr1 = term2

        term3 = self.a and self.b
        term4 = term3 or self.c
        expr2 = term4

        term5 = self.b or self.c
        term6 = self.a and term5
        expr3 = term6

        term7 = not self.a
        term8 = term7 and self.b
        term9 = term8 or self.c
        expr4 = term9

        term10 = self.a and self.b
        term11 = not term10
        term12 = term11 or self.c
        expr5 = term12

        term13 = self.b and self.c
        term14 = self.a or term13
        expr6 = term14

        term15 = self.a or self.b
        term16 = term15 and self.c
        expr7 = term16

        term17 = not self.a
        term18 = term17 or self.b
        term19 = term18 and self.c
        expr8 = term19

        term20 = self.a or self.b
        term21 = not term20
        term22 = term21 and self.c
        expr9 = term22

        term23 = not self.b
        term24 = self.a and term23
        term25 = term24 or self.c
        expr10 = term25

        return [
            ("a and b or c", expr1),
            ("(a and b) or c", expr2),
            ("a and (b or c)", expr3),
            ("not a and b or c", expr4),
            ("not (a and b) or c", expr5),
            ("a or b and c", expr6),
            ("(a or b) and c", expr7),
            ("not a or b and c", expr8),
            ("not (a or b) and c", expr9),
            ("a and not b or c", expr10)
        ]

if __name__ == '__main__':
    val_a = False
    val_b = True
    val_c = True
    val_d = False

    evaluator = BooleanExpressionEvaluator(val_a, val_b, val_c, val_d)
    results = evaluator.evaluate()
    print(results)