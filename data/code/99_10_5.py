class BooleanExpressionEvaluator:
    def __init__(self):
        self.a = True
        self.b = False
        self.c = True
        self.d = False

    def evaluate(self):
        results = {}

        res1 = self.a and self.b or self.c
        results["a and b or c"] = res1

        res2 = (self.a and self.b) or self.c
        results["(a and b) or c"] = res2

        res3 = self.a and (self.b or self.c)
        results["a and (b or c)"] = res3

        res4 = not self.a and self.b or self.c
        results["not a and b or c"] = res4

        res5 = not (self.a and self.b) or self.c
        results["not (a and b) or c"] = res5

        res6 = self.a or self.b and self.c
        results["a or b and c"] = res6

        res7 = (self.a or self.b) and self.c
        results["(a or b) and c"] = res7

        res8 = not self.a or self.b and self.c
        results["not a or b and c"] = res8

        res9 = not (self.a or self.b) and self.c
        results["not (a or b) and c"] = res9

        res10 = self.a and not self.b or self.c
        results["a and not b or c"] = res10

        res11 = (self.a or self.b) and not self.c
        results["(a or b) and not c"] = res11

        res12 = not self.a or self.b and not self.c
        results["not a or b and not c"] = res12

        return results

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    output = evaluator.evaluate()
    print(output)