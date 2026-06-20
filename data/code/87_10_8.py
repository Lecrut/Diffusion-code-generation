class LogicCombiner:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    combiner = LogicCombiner()
    results = {
        (True, True): combiner.evaluate(True, True),
        (True, False): combiner.evaluate(True, False),
        (False, True): combiner.evaluate(False, True),
        (False, False): combiner.evaluate(False, False)
    }
    for input_pair, result in results.items():
        print(f"evaluate({input_pair[0]}, {input_pair[1]}): {result}")