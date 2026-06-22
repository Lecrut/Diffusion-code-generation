class ConditionEvaluator:
    def __init__(self, first: bool, second: bool):
        self.first = first
        self.second = second
        self._truth_table = {
            (True, True): True,
            (True, False): True,
            (False, True): True,
            (False, False): False,
        }

    def evaluate(self):
        state = (self.first, self.second)
        if state not in self._truth_table:
            raise ValueError("Unsupported state combination")
        return self._truth_table[state]

if __name__ == '__main__':
    evaluator = ConditionEvaluator(False, False)
    result = evaluator.evaluate()
    print(result)