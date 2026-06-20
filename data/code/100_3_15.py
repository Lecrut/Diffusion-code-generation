class LogicChecker:
    def evaluate(self, bool_list):
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    sample1 = [True, True, True]
    sample2 = [False, False, False]
    sample3 = [True, False, True]
    sample4 = []
    sample5 = [True, True, True, True]

    print(f"Sample 1: {sample1}, Result: {checker.evaluate(sample1)}")
    print(f"Sample 2: {sample2}, Result: {checker.evaluate(sample2)}")
    print(f"Sample 3: {sample3}, Result: {checker.evaluate(sample3)}")
    print(f"Sample 4: {sample4}, Result: {checker.evaluate(sample4)}")
    print(f"Sample 5: {sample5}, Result: {checker.evaluate(sample5)}")