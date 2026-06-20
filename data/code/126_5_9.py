class EqualityChecker:
    def verify_value_equality(self, a, b):
        return a == b and type(a) == type(b)

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.verify_value_equality(5, 5))
    print(checker.verify_value_equality(5, '5'))
    print(checker.verify_value_equality([1, 2], [1, 2]))
    print(checker.verify_value_equality([1, 2], [2, 1]))