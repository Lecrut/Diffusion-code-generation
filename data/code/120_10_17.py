class EqualityChecker:
    @staticmethod
    def are_equal(a, b):
        if type(a) is not type(b):
            return False
        return a is b or a == b

if __name__ == '__main__':
    print(EqualityChecker.are_equal(5, 5))
    print(EqualityChecker.are_equal(10, 5))
    print(EqualityChecker.are_equal("hello", "hello"))
    print(EqualityChecker.are_equal(1, 2))