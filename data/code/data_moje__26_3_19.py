class VoterEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        return self.age >= 18

if __name__ == '__main__':
    checker1 = VoterEligibilityChecker(20)
    print(checker1.is_eligible())

    checker2 = VoterEligibilityChecker(17)
    print(checker2.is_eligible())

    checker3 = VoterEligibilityChecker("18")
    print(checker3.is_eligible())

    checker4 = VoterEligibilityChecker(18.0)
    print(checker4.is_eligible())

    checker5 = VoterEligibilityChecker(18)
    print(checker5.is_eligible())