import datetime

class VotingEligibilityManager:
    def __init__(self, voting_age=18):
        self.voting_age = voting_age
        self.min_legal_age = 16
        self.max_voter_age = 120

    def _validate_age_input(self, age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0 or age > self.max_voter_age:
            raise ValueError("Age must be a realistic positive number")

    def check_eligibility(self, age, citizenship=False, felony=False):
        self._validate_age_input(age)
        if not citizenship:
            return False
        if felony:
            return False
        if age < self.min_legal_age:
            return False
        if age < self.voting_age:
            return False
        return True

    def calculate_years_until_eligible(self, age, citizenship=True, felony=False):
        self._validate_age_input(age)
        if not citizenship:
            raise ValueError("Non-citizens are not eligible to vote")
        if felony:
            raise ValueError("Individuals with felony convictions may have restrictions")
        if age < self.min_legal_age:
            return self.voting_age - age
        if age >= self.voting_age:
            return 0
        return self.voting_age - age

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    test_cases = [
        (15, True, False),
        (17, True, False),
        (18, True, False),
        (25, False, False),
        (30, True, True),
        (50, True, False),
    ]
    for age, citizen, felony in test_cases:
        result = manager.check_eligibility(age, citizen, felony)
        print(f"Age: {age}, Citizen: {citizen}, Felony: {felony} -> Eligible: {result}")
    young_voter = 17
    years_needed = manager.calculate_years_until_eligible(young_voter, True, False)
    print(f"Years until eligible for age {young_voter}: {years_needed}")
    mature_voter = 30
    years_for_mature = manager.calculate_years_until_eligible(mature_voter, True, False)
    print(f"Years until eligible for age {mature_voter}: {years_for_mature}")