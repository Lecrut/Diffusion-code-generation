class ValueChecker:
    def are_values_unequal(self, value1: any, value2: any) -> bool:
        return value1 != value2

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_values_unequal(42, 43)
    print(result)