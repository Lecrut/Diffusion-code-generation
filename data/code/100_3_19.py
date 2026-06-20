class LogicChecker:
    def evaluate(self, bool_list):
        if not isinstance(bool_list, list) or not all(isinstance(x, bool) for x in bool_list):
            raise ValueError("Input must be a list of boolean values")
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    sample1 = [True, True, True]
    sample2 = [True, False, True]
    sample3 = [False, False]
    sample4 = []
    sample5 = [True]

    print(f"Sample 1: {sample1}, Result: {checker.evaluate(sample1)}")
    print(f"Sample 2: {sample2}, Result: {checker.evaluate(sample2)}")
    print(f"Sample 3: {sample3}, Result: {checker.evaluate(sample3)}")
    print(f"Sample 4: {sample4}, Result: {checker.evaluate(sample4)}")
    print(f"Sample 5: {sample5}, Result: {checker.evaluate(sample5)}")