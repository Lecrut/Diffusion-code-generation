class EqualityChecker:
    @staticmethod
    def are_values_equal(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.are_values_equal("Hello", "hello"))
    print(EqualityChecker.are_values_equal("Python", "python"))
    print(EqualityChecker.are_values_equal("World", "earth"))
    print(EqualityChecker.are_values_equal("Test", "tEsT"))
    print(EqualityChecker.are_values_equal("Apple", "apple"))