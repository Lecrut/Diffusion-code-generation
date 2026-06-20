class AccessChecker:
    MIN_AGE = 18

    @staticmethod
    def check_or_condition(age, permission):
        return age >= AccessChecker.MIN_AGE or permission

if __name__ == '__main__':
    sample_age = 25
    sample_permission = True
    result = AccessChecker.check_or_condition(sample_age, sample_permission)
    print(result)