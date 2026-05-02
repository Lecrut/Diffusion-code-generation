class ValueChecker:
    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    value1 = 10
    value2 = 20
    value3 = 10
    value4 = 10
    print(f"Are {value1} and {value2} different? {checker.are_different(value1, value2)}")
    print(f"Are {value1} and {value3} different? {checker.are_different(value1, value3)}")
    print(f"Are {value3} and {value4} different? {checker.are_different(value3, value4)}")