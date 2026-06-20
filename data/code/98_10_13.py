CONDITIONS = [True, False, True]

class ConditionChecker:
    def check_all(self, conditions):
        return all(conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_all(CONDITIONS)
    print(f"All conditions met: {result}")