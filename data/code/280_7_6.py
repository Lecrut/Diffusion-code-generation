class NumberEvaluator:
    def evaluate(self, number):
        if number % 2 == 0:
            return f"{number} is even"
        else:
            return f"{number} is odd"

if __name__ == '__main__':
    evaluator = NumberEvaluator()
    for i in range(15):
        print(evaluator.evaluate(i))