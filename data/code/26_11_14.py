import datetime
from typing import Optional

class VotingEligibilityManager:
    VOTING_AGE = 18
    DEFAULT_DISQUALIFICATION_YEARS = 5

    def __init__(self, age: int, has_criminal_record: bool = False, felony_disqualification_years: int = 0):
        self.age = age
        self.has_criminal_record = has_criminal_record
        self.felony_disqualification_years = felony_disqualification_years

    def check_age_eligibility(self) -> bool:
        return self.age >= self.VOTING_AGE

    def check_legal_eligibility(self) -> bool:
        if not self.has_criminal_record:
            return True
        if self.felony_disqualification_years >= self.DEFAULT_DISQUALIFICATION_YEARS:
            return True
        return False

    def is_eligible(self) -> bool:
        if not self.check_age_eligibility():
            return False
        return self.check_legal_eligibility()

    def get_eligibility_status(self) -> str:
        if not self.check_age_eligibility():
            return f"Ineligible: Age {self.age} is below voting age {self.VOTING_AGE}"
        if self.has_criminal_record and self.felony_disqualification_years < self.DEFAULT_DISQUALIFICATION_YEARS:
            return f"Ineligible: Felony disqualification period of {self.felony_disqualification_years} years has not passed"
        return f"Eligible: Age {self.age}, No active legal disqualification"

if __name__ == '__main__':
    manager_adult = VotingEligibilityManager(25, False)
    print(manager_adult.is_eligible())
    print(manager_adult.get_eligibility_status())

    manager_minor = VotingEligibilityManager(16, False)
    print(manager_minor.is_eligible())
    print(manager_minor.get_eligibility_status())

    manager_convict = VotingEligibilityManager(30, True, 3)
    print(manager_convict.is_eligible())
    print(manager_convict.get_eligibility_status())

    manager_fully_served = VotingEligibilityManager(30, True, 6)
    print(manager_fully_served.is_eligible())
    print(manager_fully_served.get_eligibility_status())