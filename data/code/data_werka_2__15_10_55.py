class EqualityEngine:
    @staticmethod
    def check_equality(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityEngine.check_equality(10, 20))          # False
    print(EqualityEngine.check_equality("hello", "hello"))  # True
    print(EqualityEngine.check_equality([1, 2], [1, 2]))    # True
    print(EqualityEngine.check_equality({"a": 1}, {"b": 1}))# False