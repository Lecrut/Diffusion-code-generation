class ConditionChecker:
    def check_condition(self, a, b):
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Test case 1: Equal integers
    result1 = checker.check_condition(5, 5)
    print(f"check_condition(5, 5) -> {result1}")
    
    # Test case 2: Different strings
    result2 = checker.check_condition("hello", "world")
    print(f"check_condition('hello', 'world') -> {result2}")
    
    # Test case 3: Equal floats
    result3 = checker.check_condition(3.14, 3.14)
    print(f"check_condition(3.14, 3.14) -> {result3}")