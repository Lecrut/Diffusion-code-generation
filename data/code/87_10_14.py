class LogicCombiner:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    result1 = LogicCombiner.evaluate(True, True)
    print(f"evaluate(True, True): {result1}")
    result2 = LogicCombiner.evaluate(True, False)
    print(f"evaluate(True, False): {result2}")
    result3 = LogicCombiner.evaluate(False, True)
    print(f"evaluate(False, True): {result3}")
    result4 = LogicCombiner.evaluate(False, False)
    print(f"evaluate(False, False): {result4}")