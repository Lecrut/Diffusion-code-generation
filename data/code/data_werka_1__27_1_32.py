class ValueChecker:
    def are_unequal(self, value1: object, value2: object) -> bool:
        return value1 != value2

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_unequal(42, 3.14)
    print(result)