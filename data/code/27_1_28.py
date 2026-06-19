class ValueChecker:
    def __init__(self, value1: any, value2: any):
        self.value1 = value1
        self.value2 = value2

    def are_unequal(self) -> bool:
        return self.value1 != self.value2

if __name__ == '__main__':
    checker = ValueChecker(42, '42')
    print(checker.are_unequal())