class VotingEligibilityManager:
    def __init__(self, minimum_age: int = 18):
        self.minimum_age = minimum_age

    def _is_age_valid(self, age: int) -> bool:
        return age >= self.minimum_age

    def _is_disqualified(self, conviction_status: str, incarceration_status: bool) -> bool:
        if incarceration_status:
            return True
        if conviction_status.lower() == 'yes':
            return True
        return False

    def check_eligibility(self, age: int, convicted: bool = False, incarcerated: bool = False) -> bool:
        if not isinstance(age, int) or age < 0:
            return False
        if self._is_disqualified(str(convicted).lower(), incarcerated):
            return False
        return self._is_age_valid(age)

if __name__ == '__main__':
    manager = VotingEligibilityManager(minimum_age=18)
    
    eligible_person_1 = manager.check_eligibility(age=20, convicted=False, incarcerated=False)
    print(f"Eligibility for 20-year-old, no convictions: {eligible_person_1}")
    
    ineligible_person_2 = manager.check_eligibility(age=16, convicted=False, incarcerated=False)
    print(f"Eligibility for 16-year-old, no convictions: {ineligible_person_2}")
    
    ineligible_person_3 = manager.check_eligibility(age=25, convicted=True, incarcerated=False)
    print(f"Eligibility for 25-year-old, convicted: {ineligible_person_3}")
    
    ineligible_person_4 = manager.check_eligibility(age=25, convicted=False, incarcerated=True)
    print(f"Eligibility for 25-year-old, incarcerated: {ineligible_person_4}")
    
    result_age_check = manager._is_age_valid(18)
    print(f"Age validation for 18: {result_age_check}")