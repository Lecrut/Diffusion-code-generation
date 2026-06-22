class VotingEligibilityChecker:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        if self.age >= 18:
            return True
        return False

if __name__ == '__main__':
    test_ages = [17, 18, 19, 25, 18.5, "18", 100]
    for age in test_ages:
        checker = VotingEligibilityChecker(age)
        result = checker.is_eligible()
        print(f"Age: {age}, Eligible: {result}")