class BooleanExpressionEvaluator:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate_group_1(self):
        term1 = (self.a > self.b)
        term2 = (self.c < self.d)
        term3 = not (self.a == self.b)
        return (term1 and term2) or term3

    def evaluate_group_2(self):
        left = (self.a == self.b) or (self.c > self.d)
        right = not (self.a < self.b)
        return left and right

    def evaluate_group_3(self):
        inner_and = (self.a > self.b) and (self.c == self.d)
        left = not inner_and
        right = (self.a < self.b)
        return left or right

    def evaluate_group_4(self):
        cond1 = (self.a != self.b)
        cond2 = (self.c > self.d)
        cond3 = (self.a == self.c)
        return cond1 and (cond2 or cond3)

    def evaluate_group_5(self):
        val1 = (self.a + self.b) > self.c
        val2 = (self.d - self.a) < self.b
        return val1 and val2

    def evaluate_group_6(self):
        val1 = self.a > self.b
        val2 = self.c < self.d
        inner = val1 and val2
        return not inner

    def evaluate_group_7(self):
        val1 = self.a != self.b
        val2 = self.c > self.d
        val3 = self.a < self.b
        return (val1 or val2) and val3

    def evaluate_group_8(self):
        val1 = (self.a + self.b) > (self.c * self.d)
        val2 = not (self.a == 0)
        return val1 and val2

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator(12, 8, 25, 10)
    print(evaluator.evaluate_group_1())
    print(evaluator.evaluate_group_2())
    print(evaluator.evaluate_group_3())
    print(evaluator.evaluate_group_4())
    print(evaluator.evaluate_group_5())
    print(evaluator.evaluate_group_6())
    print(evaluator.evaluate_group_7())
    print(evaluator.evaluate_group_8())