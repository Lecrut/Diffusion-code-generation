class ValueChecker:

    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    VALUE_ONE = 5
    VALUE_TWO = 10
    VALUE_THREE = 7
    VALUE_FOUR = 3.14
    VALUE_FIVE = 3.14
    print(checker.are_different(VALUE_ONE, VALUE_TWO))
    print(checker.are_different(VALUE_THREE, VALUE_THREE))
    print(checker.are_different(VALUE_TWO, VALUE_FOUR))
    print(checker.are_different(VALUE_FIVE, VALUE_FIVE))