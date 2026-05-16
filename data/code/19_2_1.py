class ConditionChecker:
    def check_condition(self, a, b):
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    result1 = checker.check_condition(5, 5)
    result2 = checker.check_condition(10, 20)
    result3 = checker.check_condition("hello", "hello")
    result4 = checker.check_condition(3.14, 3.14159)
    print(f"5 == 5: {result1}")
    print(f"10 == 20: {result2}")
    print(f"'hello' == 'hello': {result3}")
    print(f"3.14 == 3.14159: {result4}")