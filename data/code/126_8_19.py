class EqualityChecker:
    def are_values_equal(self, a, b):
        return a == b

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_values_equal(5, 5))
    print(checker.are_values_equal(3, 7))