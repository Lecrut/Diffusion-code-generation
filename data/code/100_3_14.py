class LogicChecker:
    def evaluate(self, bool_list):
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    sample_values = [
        [True, True, True],
        [True, False, True],
        [False, False],
        [],
        [True]
    ]
    for idx, sample in enumerate(sample_values):
        print(f"Sample {idx + 1}: {sample}, Result: {checker.evaluate(sample)}")