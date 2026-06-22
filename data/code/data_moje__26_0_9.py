class VoterEligibilityChecker:
    def __init__(self, minimum_age):
        self.minimum_age = minimum_age

    def is_eligible(self, age):
        return age >= self.minimum_age

    def check_multiple_ages(self, ages):
        return [self.is_eligible(age) for age in ages]

def is_eligible_to_vote(age):
    checker = VoterEligibilityChecker(18)
    return checker.is_eligible(age)

if __name__ == '__main__':
    checker = VoterEligibilityChecker(18)
    print(checker.is_eligible(15))
    print(checker.is_eligible(18))
    print(checker.is_eligible(25))
    print(is_eligible_to_vote(17))
    print(is_eligible_to_vote(20))