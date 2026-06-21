import datetime

class VotingEligibilityManager:
    def __init__(self, voting_age=18):
        self.voting_age = voting_age
        self.records = {}

    def add_record(self, voter_id, birth_date, citizenship_status="citizen"):
        if not isinstance(birth_date, datetime.date):
            birth_date = datetime.date.fromisoformat(birth_date)
        self.records[voter_id] = {
            "birth_date": birth_date,
            "citizenship_status": citizenship_status,
        }

    def is_eligible(self, voter_id):
        if voter_id not in self.records:
            return False
        record = self.records[voter_id]
        if record["citizenship_status"] != "citizen":
            return False
        today = datetime.date.today()
        birth_date = record["birth_date"]
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age >= self.voting_age

    def get_eligible_voters(self):
        return [
            voter_id for voter_id in self.records if self.is_eligible(voter_id)
        ]

if __name__ == "__main__":
    manager = VotingEligibilityManager(voting_age=18)

    today = datetime.date.today()
    eligible_birth = datetime.date(today.year - 20, today.month, today.day)
    ineligible_birth = datetime.date(today.year - 15, today.month, today.day)
    non_citizen_birth = datetime.date(today.year - 25, today.month, today.day)

    manager.add_record("voter_001", eligible_birth)
    manager.add_record("voter_002", ineligible_birth)
    manager.add_record("voter_003", non_citizen_birth, citizenship_status="alien")

    print(manager.is_eligible("voter_001"))
    print(manager.is_eligible("voter_002"))
    print(manager.is_eligible("voter_003"))
    print(manager.get_eligible_voters())