class VotingEligibilityChecker:
    def check_eligibility(self, age):
        if not isinstance(age, int):
            return False
        return age >= 18

if __name__ == '__main__':
    checker = VotingEligibilityChecker()
    test_ages = [17, 18, 19, 25, 30, "20", 17.5, 100]
    for age in test_ages:
        print(checker.check_eligibility(age))