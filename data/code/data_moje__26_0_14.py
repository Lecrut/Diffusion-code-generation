class VotingEligibilityChecker:
    VOTING_THRESHOLD = 18

    def __init__(self, age):
        self.age = age

    def check(self):
        return self.age >= self.VOTING_THRESHOLD

if __name__ == '__main__':
    checker1 = VotingEligibilityChecker(17)
    print(checker1.check())
    checker2 = VotingEligibilityChecker(18)
    print(checker2.check())
    checker3 = VotingEligibilityChecker(30)
    print(checker3.check())