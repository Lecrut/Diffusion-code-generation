class BooleanEvaluator:
    def __init__(self):
        self.var1 = True
        self.var2 = False
        self.var3 = True

    def determine_outcome(self):
        return (self.var1 and not self.var2) or (self.var3 ^ self.var2)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.determine_outcome()
    print(f"Outcome: {result}")