class VotingEligibilityManager:
    def __init__(self, current_date=None):
        self._current_date = current_date
        self._eligible_records = {}
        self._ineligible_records = {}

    def _calculate_age(self, birth_date, reference_date):
        year_diff = reference_date.year - birth_date.year
        month_diff = reference_date.month - birth_date.month
        day_diff = reference_date.day - birth_date.day
        age = year_diff - (1 if (month_diff < 0 or (month_diff == 0 and day_diff < 0)) else 0)
        return age

    def _is_legal_date(self, date):
        if date is None:
            return False
        if date.year < 1:
            return False
        if date.month < 1 or date.month > 12:
            return False
        if date.day < 1 or date.day > 31:
            return False
        return True

    def _validate_input(self, name, birth_date, legal_constraints):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if birth_date is None or not self._is_legal_date(birth_date):
            raise ValueError("Invalid birth date")
        if not isinstance(legal_constraints, dict):
            raise ValueError("Legal constraints must be a dictionary")
        if 'min_age' not in legal_constraints:
            raise ValueError("Legal constraints must include min_age")
        if 'max_age' not in legal_constraints:
            raise ValueError("Legal constraints must include max_age")
        if legal_constraints['min_age'] < 0 or legal_constraints['min_age'] > legal_constraints.get('max_age', 150):
            raise ValueError("Invalid min_age in constraints")
        if legal_constraints.get('max_age', 150) < legal_constraints['min_age']:
            raise ValueError("Invalid max_age in constraints")

    def check_eligibility(self, name, birth_date, legal_constraints=None, current_date=None):
        if current_date is None:
            current_date = self._get_current_date()
        
        self._validate_input(name, birth_date, legal_constraints or {'min_age': 18, 'max_age': 120})
        
        min_age = legal_constraints.get('min_age', 18)
        max_age = legal_constraints.get('max_age', 120)
        
        age = self._calculate_age(birth_date, current_date)
        
        is_eligible = min_age <= age <= max_age
        
        if is_eligible:
            self._eligible_records[name] = {
                'age': age,
                'birth_date': birth_date,
                'current_date': current_date
            }
        else:
            self._ineligible_records[name] = {
                'age': age,
                'birth_date': birth_date,
                'current_date': current_date,
                'reason': 'Age outside constraints' if age < min_age else 'Age outside constraints'
            }
        
        return is_eligible

    def get_eligible_voters(self):
        return list(self._eligible_records.keys())

    def get_ineligible_voters(self):
        return list(self._ineligible_records.keys())

    def get_voter_details(self, name):
        if name in self._eligible_records:
            return {
                'status': 'eligible',
                'details': self._eligible_records[name]
            }
        if name in self._ineligible_records:
            return {
                'status': 'ineligible',
                'details': self._ineligible_records[name]
            }
        return {
            'status': 'unknown',
            'details': None
        }

    def reset_records(self):
        self._eligible_records.clear()
        self._ineligible_records.clear()

    def _get_current_date(self):
        from datetime import date
        return date.today()

if __name__ == '__main__':
    from datetime import date
    
    manager = VotingEligibilityManager()
    
    eligibility_result = manager.check_eligibility(
        "Alice",
        date(1990, 5, 15),
        {'min_age': 18, 'max_age': 100}
    )
    
    print(eligibility_result)
    
    eligible_voters = manager.get_eligible_voters()
    print(eligible_voters)
    
    voter_details = manager.get_voter_details("Alice")
    print(voter_details)
    
    manager.check_eligibility(
        "Bob",
        date(2010, 1, 1),
        {'min_age': 18, 'max_age': 100}
    )
    
    ineligible_voters = manager.get_ineligible_voters()
    print(ineligible_voters)
    
    bob_details = manager.get_voter_details("Bob")
    print(bob_details)