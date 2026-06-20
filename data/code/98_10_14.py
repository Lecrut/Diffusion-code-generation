class ConditionChecker:
    def check_all(self, conditions):
        return all(conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    sample_conditions = [True, False, True]
    print(checker.check_all(sample_conditions))