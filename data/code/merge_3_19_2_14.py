class ConditionChecker:
    def check_condition(self, a, b):
        return a == b

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Test case 1: Equal values (integers)
    result_1 = checker.check_condition(5, 5)
    print(f"check_condition(5, 5) returned {result_1}")

    # Test case 2: Different integers
    result_2 = checker.check_condition(3, 7)
    print(f"check_condition(3, 7) returned {result_2}")

    # Test case 3: Equal strings
    result_3 = checker.check_condition("hello", "hello")
    print(f'check_condition("hello", "hello") returned {result_3}')

    # Test case 4: Different types that might look similar but are not (e.g., int vs float)
    result_4 = checker.check_condition(2, 2.0)
    print(f"check_condition(2, 2.0) returned {result_4}")