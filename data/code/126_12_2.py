class ValueChecker:
    def is_equal(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    value1 = 10
    value2 = 10
    value3 = 5
    value4 = 5.0
    value5 = "hello"
    print(f"Is {value1} equal to {value2}? {checker.is_equal(value1, value2)}")
    print(f"Is {value1} equal to {value3}? {checker.is_equal(value1, value3)}")
    print(f"Is {value4} equal to {value2}? {checker.is_equal(value4, value2)}")
    print(f"Is {value5} equal to {value1}? {checker.is_equal(value5, value1)}")