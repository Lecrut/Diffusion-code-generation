class BooleanExpressionEvaluator:
    def __init__(self, a, b, c, d):
        if not all(isinstance(x, bool) for x in [a, b, c, d]):
            raise ValueError("Inputs must be boolean")
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self):
        res = {}
        res["a_and_b_or_c"] = self.a and self.b or self.c
        res["paren_and_or"] = (self.a and self.b) or self.c
        res["a_and_paren_or"] = self.a and (self.b or self.c)
        res["not_a_and_b_or_c"] = not self.a and self.b or self.c
        res["not_paren_and_or"] = not (self.a and self.b) or self.c
        res["a_or_b_and_c"] = self.a or self.b and self.c
        res["paren_or_and"] = (self.a or self.b) and self.c
        res["not_a_or_b_and_c"] = not self.a or self.b and self.c
        res["not_paren_or_and"] = not (self.a or self.b) and self.c
        res["a_and_not_b_or_c"] = self.a and not self.b or self.c
        res["d_and_not_c"] = self.d and not self.c
        res["not_d_or_c"] = not self.d or self.c
        res["a_xor_b"] = (self.a or self.b) and not (self.a and self.b)
        res["not_a_or_not_b"] = not self.a or not self.b
        res["a_and_b_and_c"] = self.a and self.b and self.c
        return res

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator(True, False, True, False)
    results = evaluator.evaluate()
    print(results)