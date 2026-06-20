class LogicCombiner:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    combiner = LogicCombiner()
    result1 = combiner.evaluate(True, False)
    print(f"evaluate(True, False): {result1}")
    result2 = combiner.evaluate(False, True)
    print(f"evaluate(False, True): {result2}")