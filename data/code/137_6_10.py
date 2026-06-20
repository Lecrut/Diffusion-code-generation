class RangeChecker:
    def check_range(self):
        value = 7
        return 1 <= value <= 10

if __name__ == '__main__':
    checker = RangeChecker()
    print(checker.check_range())