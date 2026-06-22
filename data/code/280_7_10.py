class NumberEvaluator:
    def evaluate(self, number):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

if __name__ == '__main__':
    evaluator = NumberEvaluator()
    for i in range(15):
        evaluator.evaluate(i)