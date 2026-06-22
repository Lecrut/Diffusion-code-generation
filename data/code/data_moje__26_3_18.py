class VotingEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        return self.age >= 18

if __name__ == '__main__':
    checker1 = VotingEligibilityChecker(17)
    print(checker1.is_eligible())
    checker2 = VotingEligibilityChecker(18)
    print(checker2.is_eligible())
    checker3 = VotingEligibilityChecker(21)
    print(checker3.is_eligible())
    checker4 = VotingEligibilityChecker(15)
    print(checker4.is_eligible())
    checker5 = VotingEligibilityChecker("20")
    print(checker5.is_eligible())