class LogicCombiner:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    combiner = LogicCombiner()
    result1 = combiner.evaluate(True, True)
    print(f"evaluate(True, True): {result1}")
    result2 = combiner.evaluate(False, False)
    print(f"evaluate(False, False): {result2}")