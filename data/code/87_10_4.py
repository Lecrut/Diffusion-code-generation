class LogicCombiner:
    def evaluate(self, a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    combiner = LogicCombiner()
    result1 = combiner.evaluate(True, True)
    print(f"evaluate(True, True): {result1}")
    result2 = combiner.evaluate(True, False)
    print(f"evaluate(True, False): {result2}")
    result3 = combiner.evaluate(False, True)
    print(f"evaluate(False, True): {result3}")
    result4 = combiner.evaluate(False, False)
    print(f"evaluate(False, False): {result4}")