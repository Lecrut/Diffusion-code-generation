class ConditionEvaluator:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def evaluate(self):
        if self.x > 10 and self.y < 5:
            return "First branch executed"
        elif self.z == 0:
            return "Second branch executed"
        elif self.x == self.y:
            return "Third branch executed"
        else:
            return "Default branch executed"

    def get_sum(self):
        return self.x + self.y + self.z

if __name__ == '__main__':
    evaluator = ConditionEvaluator(15, 3, 5)
    print(evaluator.evaluate())
    print(evaluator.get_sum())
    
    evaluator2 = ConditionEvaluator(5, 12, 0)
    print(evaluator2.evaluate())
    print(evaluator2.get_sum())