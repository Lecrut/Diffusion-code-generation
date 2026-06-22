class VotingEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        return isinstance(self.age, int) and self.age >= 18

if __name__ == '__main__':
    checker1 = VotingEligibilityChecker(20)
    print(checker1.is_eligible())
    checker2 = VotingEligibilityChecker(17)
    print(checker2.is_eligible())
    checker3 = VotingEligibilityChecker(18)
    print(checker3.is_eligible())
    checker4 = VotingEligibilityChecker(18.5)
    print(checker4.is_eligible())