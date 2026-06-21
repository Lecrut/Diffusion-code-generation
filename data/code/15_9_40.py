class ValueChecker:

    def are_equal(self, a, b):
        try:
            return a == b
        except TypeError:
            return str(a) == str(b)
if __name__ == '__main__':
    checker = ValueChecker()
    value1 = 42
    value2 = '42'
    value3 = 3.14
    value4 = '3.14'
    value5 = [1, 2, 3]
    value6 = (1, 2, 3)
    print(checker.are_equal(value1, value2))
    print(checker.are_equal(value3, value4))
    print(checker.are_equal(value5, value6))