class AccessChecker:
    MIN_AGE = 18

    @staticmethod
    def check_or_condition(age, permission):
        return age >= AccessChecker.MIN_AGE or permission
if __name__ == '__main__':
    result = AccessChecker.check_or_condition(25, True)
    print(result)