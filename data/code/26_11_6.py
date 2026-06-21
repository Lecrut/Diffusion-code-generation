class VotingEligibilityManager:
    VOTING_AGE = 18
    LEGAL_RESIDENCY_REQUIREMENT = 5

    def __init__(self):
        self.records = {}

    def register_voter(self, voter_id, age, years_resided):
        if age < 0 or years_resided < 0:
            raise ValueError("Age and years_resided must be non-negative")
        self.records[voter_id] = {
            "age": age,
            "years_resided": years_resided,
            "eligible": self._check_eligibility(age, years_resided)
        }
        return self.records[voter_id]["eligible"]

    def _check_eligibility(self, age, years_resided):
        return age >= self.VOTING_AGE and years_resided >= self.LEGAL_RESIDENCY_REQUIREMENT

    def is_eligible(self, voter_id):
        if voter_id not in self.records:
            return False
        return self.records[voter_id]["eligible"]

    def get_voter_record(self, voter_id):
        if voter_id not in self.records:
            return None
        record = self.records[voter_id].copy()
        return record

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.register_voter("V001", 20, 10)
    manager.register_voter("V002", 17, 20)
    manager.register_voter("V003", 25, 3)
    print(manager.is_eligible("V001"))
    print(manager.is_eligible("V002"))
    print(manager.is_eligible("V003"))
    print(manager.get_voter_record("V001"))