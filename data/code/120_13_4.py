class ValueChecker:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    value1 = 10
    value2 = 10
    value3 = 5
    value4 = "hello"
    result1 = checker.check_equality(value1, value2)
    result2 = checker.check_equality(value1, value3)
    result3 = checker.check_equality(value4, value1)
    print(f"Is {value1} equal to {value2}? {result1}")
    print(f"Is {value1} equal to {value3}? {result2}")
    print(f"Is '{value4}' equal to {value1}? {result3}")