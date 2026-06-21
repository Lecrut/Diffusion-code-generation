class IntegerPropertyChecker:
    def __init__(self, first: int, second: int, third: int):
        self.first = first
        self.second = second
        self.third = third

    def check_positivity(self) -> bool:
        return self.first > 0

    def check_evenness(self) -> bool:
        return self.second % 2 == 0

    def check_divisibility(self) -> bool:
        if self.first == 0:
            return False
        return self.third % self.first == 0

    def run_all_checks(self) -> tuple:
        return (self.check_positivity(), self.check_evenness(), self.check_divisibility())

if __name__ == '__main__':
    checker = IntegerPropertyChecker(first=7, second=9, third=21)
    print(checker.run_all_checks())
    print(checker.check_positivity())
    print(checker.check_evenness())
    print(checker.check_divisibility())