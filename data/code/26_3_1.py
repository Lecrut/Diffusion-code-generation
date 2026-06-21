class VotingEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int) or isinstance(self.age, bool):
            return False
        return self.age >= 18

if __name__ == '__main__':
    checker = VotingEligibilityChecker(20)
    print(checker.is_eligible())