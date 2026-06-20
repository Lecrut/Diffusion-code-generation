class ShortCircuitLogic:
    @staticmethod
    def evaluate_and(x: bool, y: bool) -> bool:
        return x and y

if __name__ == '__main__':
    result = ShortCircuitLogic.evaluate_and(True, False)
    print(result)