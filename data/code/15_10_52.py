class EqualityChecker:
    @staticmethod
    def check_equality(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.check_equality(10, 20))          # False
    print(EqualityChecker.check_equality("hello", "hello"))  # True
    print(EqualityChecker.check_equality([1, 2], [1, 2]))    # True
    print(EqualityChecker.check_equality({"a": 1}, {"b": 1}))# False