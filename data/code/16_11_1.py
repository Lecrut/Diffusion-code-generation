class NumberChecker:
    def check_positivity(self, value):
        return value > 0
if __name__ == '__main__':
    checker = NumberChecker()
    value1 = 10
    result1 = checker.check_positivity(value1)
    print(f"Is {value1} positive? {result1}")
    value2 = -5
    result2 = checker.check_positivity(value2)
    print(f"Is {value2} positive? {result2}")
    value3 = 0
    result3 = checker.check_positivity(value3)
    print(f"Is {value3} positive? {result3}")
    value4 = 99.5
    result4 = checker.check_positivity(value4)
    print(f"Is {value4} positive? {result4}")