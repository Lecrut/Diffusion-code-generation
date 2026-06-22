class VoterEligibilityChecker:
    def __init__(self, minimum_age=18):
        self.minimum_age = minimum_age

    def is_eligible(self, age):
        return age >= self.minimum_age

if __name__ == '__main__':
    checker = VoterEligibilityChecker(minimum_age=18)
    result1 = checker.is_eligible(17)
    result2 = checker.is_eligible(18)
    result3 = checker.is_eligible(20)
    print(result1)
    print(result2)
    print(result3)