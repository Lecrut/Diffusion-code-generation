class VoterEligibilityChecker:
    def __init__(self, voting_age=18):
        self.voting_age = voting_age

    def check_eligibility(self, age):
        return age >= self.voting_age

    def get_minimum_age(self):
        return self.voting_age

if __name__ == '__main__':
    checker = VoterEligibilityChecker()
    print(checker.check_eligibility(17))
    print(checker.check_eligibility(18))
    print(checker.check_eligibility(25))
    print(checker.get_minimum_age())