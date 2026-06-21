class VoterEligibilityChecker:
    VOTING_AGE = 18

    def __init__(self, age):
        if not isinstance(age, (int, float)):
            raise TypeError("Age must be a numeric value")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age

    def is_eligible(self):
        return self.age >= self.VOTING_AGE

def check_eligibility(age):
    checker = VoterEligibilityChecker(age)
    return checker.is_eligible()

if __name__ == '__main__':
    test_cases = [15, 18, 25, 17.9, 100, -1, "not_a_number"]
    for case in test_cases:
        try:
            result = check_eligibility(case)
            print(result)
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")