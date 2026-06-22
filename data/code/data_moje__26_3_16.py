class VotingEligibilityChecker:
    def is_eligible(self, age):
        if not isinstance(age, int) or isinstance(age, bool):
            return False
        return age >= 18

if __name__ == '__main__':
    checker = VotingEligibilityChecker()
    print(checker.is_eligible(18))
    print(checker.is_eligible(17))
    print(checker.is_eligible(20))
    print(checker.is_eligible(18.5))
    print(checker.is_eligible(-5))
    print(checker.is_eligible("18"))
    print(checker.is_eligible(True))