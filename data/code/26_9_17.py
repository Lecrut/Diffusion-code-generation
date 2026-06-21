class VotingEligibilityChecker:
    LEGAL_VOTING_AGE = 18

    def __init__(self):
        self.threshold = self.LEGAL_VOTING_AGE

    def can_vote(self, age):
        return age > self.threshold

    def get_status(self, age):
        if self.can_vote(age):
            return True
        return False

if __name__ == '__main__':
    checker = VotingEligibilityChecker()
    print(checker.can_vote(16))
    print(checker.can_vote(18))
    print(checker.get_status(20))