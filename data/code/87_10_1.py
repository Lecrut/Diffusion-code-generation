class LogicCombiner:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    combiner = LogicCombiner()
    result = combiner.evaluate(True, False)
    print(result)