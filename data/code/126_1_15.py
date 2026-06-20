class EqualityChecker:
    def __init__(self, value):
        self.value = value

    def is_equal(self, other_value):
        return self.value == other_value

if __name__ == '__main__':
    checker1 = EqualityChecker(5)
    print(checker1.is_equal(5))
    print(checker1.is_equal(10))
    
    checker2 = EqualityChecker("hello")
    print(checker2.is_equal("hello"))
    print(checker2.is_equal("HELLO"))