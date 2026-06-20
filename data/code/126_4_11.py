class EqualityChecker:
    def check_equality(self, a, b):
        try:
            return a == b
        except TypeError:
            return False

if __name__ == '__main__':
    checker = EqualityChecker()
    
    print("Test Case 1 (Integers):")
    print(checker.check_equality(10, 10))
    print(checker.check_equality(10, 20))
    
    print("\nTest Case 2 (Strings):")
    print(checker.check_equality("hello", "hello"))
    print(checker.check_equality("hello", "world"))
    
    print("\nTest Case 3 (Lists):")
    print(checker.check_equality([1, 2], [1, 2]))
    print(checker.check_equality([1, 2], [2, 1]))