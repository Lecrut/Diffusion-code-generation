from functools import reduce
from operator import and_

EXPECTED_TRUE_RESULT = True
DEFAULT_INPUT = [True, True, True, True]

class LogicChecker:
    def evaluate(self, bool_list):
        if not bool_list:
            return EXPECTED_TRUE_RESULT
        return reduce(and_, bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    results = []
    inputs = [
        [True, True, True],
        [True, False, True],
        [False, False, False],
        [],
        [True],
        DEFAULT_INPUT
    ]
    for idx, input_data in enumerate(inputs):
        result = checker.evaluate(input_data)
        print(f"Input {idx + 1}: {result}")
    final_sample = checker.evaluate(DEFAULT_INPUT)
    print(f"Default Sample Result: {final_sample}")