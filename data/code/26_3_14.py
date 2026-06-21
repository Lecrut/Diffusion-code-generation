class VoterEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int) or isinstance(self.age, bool):
            return False
        return self.age >= 18

if __name__ == '__main__':
    checker = VoterEligibilityChecker(20)
    print(checker.is_eligible())
    checker_old = VoterEligibilityChecker(15)
    print(checker_old.is_eligible())
    checker_float = VoterEligibilityChecker(18.5)
    print(checker_float.is_eligible())