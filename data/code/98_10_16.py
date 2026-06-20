class ConditionChecker:
    def check_all(self, *conditions):
        return all(conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    result1 = checker.check_all(True, False, True)
    print(f"Result of all conditions being met: {result1}")
    result2 = checker.check_all(True, True, True)
    print(f"Result of all conditions being met: {result2}")