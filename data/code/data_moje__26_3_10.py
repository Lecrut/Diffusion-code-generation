class VotingEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        return isinstance(self.age, int) and self.age >= 18

if __name__ == '__main__':
    checker1 = VotingEligibilityChecker(17)
    checker2 = VotingEligibilityChecker(18)
    checker3 = VotingEligibilityChecker(25)
    checker4 = VotingEligibilityChecker("20")
    print(checker1.is_eligible())
    print(checker2.is_eligible())
    print(checker3.is_eligible())
    print(checker4.is_eligible())