class VoterEligibilityChecker:
    def check_eligibility(self, age):
        if not isinstance(age, int):
            return False
        return age >= 18

if __name__ == '__main__':
    checker = VoterEligibilityChecker()
    print(checker.check_eligibility(18))
    print(checker.check_eligibility(17))
    print(checker.check_eligibility(20))
    print(checker.check_eligibility("18"))
    print(checker.check_eligibility(18.5))