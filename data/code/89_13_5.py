class ShortCircuitEvaluator:
    @staticmethod
    def evaluate_and(x: bool, y: bool) -> bool:
        return x and y

if __name__ == '__main__':
    sample1 = ShortCircuitEvaluator.evaluate_and(True, False)
    print(sample1)