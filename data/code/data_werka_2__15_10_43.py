class EqualityTester:
    @staticmethod
    def test_equality(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityTester.test_equality(10, 20))          # False
    print(EqualityTester.test_equality("hello", "hello"))  # True
    print(EqualityTester.test_equality([1, 2], [1, 2]))    # True
    print(EqualityTester.test_equality({"a": 1}, {"b": 1}))# False