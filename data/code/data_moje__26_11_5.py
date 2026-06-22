class VotingEligibilityManager:
    MIN_AGE = 18
    MAX_AGE = 120
    DISQUALIFIED_CITIZENSHIP_CODES = frozenset(['FRAUDULENT', 'INVALID', 'DUAL_UNREGISTERED'])

    def __init__(self):
        self._records = {}

    def add_record(self, voter_id, age, citizenship_code):
        if not isinstance(voter_id, int) or voter_id <= 0:
            raise ValueError("Invalid voter ID")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < self.MIN_AGE:
            self._records[voter_id] = {
                'eligible': False,
                'reason': 'UNDERAGE'
            }
            return
        if age > self.MAX_AGE:
            self._records[voter_id] = {
                'eligible': False,
                'reason': 'INVALID_AGE'
            }
            return
        if citizenship_code in self.DISQUALIFIED_CITIZENSHIP_CODES:
            self._records[voter_id] = {
                'eligible': False,
                'reason': 'DISQUALIFIED_CITIZENSHIP'
            }
            return
        self._records[voter_id] = {
            'eligible': True,
            'reason': 'VALID'
        }

    def check_eligibility(self, voter_id):
        if voter_id not in self._records:
            return {
                'eligible': False,
                'reason': 'NOT_FOUND'
            }
        return self._records[voter_id]

    def get_eligible_voters(self):
        eligible = {}
        for vid, data in self._records.items():
            if data['eligible']:
                eligible[vid] = data
        return eligible

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.add_record(101, 25, 'CITIZEN')
    manager.add_record(102, 16, 'CITIZEN')
    manager.add_record(103, 45, 'INVALID')
    manager.add_record(104, 125, 'CITIZEN')
    
    result_101 = manager.check_eligibility(101)
    print(result_101)
    
    eligible_list = manager.get_eligible_voters()
    print(eligible_list)
    
    result_102 = manager.check_eligibility(102)
    print(result_102)
    
    result_999 = manager.check_eligibility(999)
    print(result_999)