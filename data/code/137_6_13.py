class NumberRangeChecker:
    def check_range(self):
        return 1 <= 5 <= 10

if __name__ == '__main__':
    checker = NumberRangeChecker()
    print(checker.check_range())