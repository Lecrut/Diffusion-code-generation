class LogicChecker:

    def evaluate(self, bool_list):
        if not bool_list:
            return False
        return all(bool_list)
if __name__ == '__main__':
    checker = LogicChecker()
    sample1 = [True, True, True]
    sample2 = [True, False, True]
    sample3 = [False, False]
    sample4 = []
    sample5 = [True]
    print(f'Sample 1: {checker.evaluate(sample1)}')
    print(f'Sample 2: {checker.evaluate(sample2)}')
    print(f'Sample 3: {checker.evaluate(sample3)}')
    print(f'Sample 4: {checker.evaluate(sample4)}')
    print(f'Sample 5: {checker.evaluate(sample5)}')