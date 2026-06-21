import datetime

class VotingEligibilityManager:
    def __init__(self, voter_id: str, birth_date: str):
        self.voter_id = voter_id
        self.birth_date = self._parse_date(birth_date)

    def _parse_date(self, date_str: str) -> datetime.date:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    def is_eligible(self, election_date: str, minimum_age: int = 18) -> bool:
        election_dt = datetime.datetime.strptime(election_date, "%Y-%m-%d").date()
        age_at_election = election_dt.year - self.birth_date.year - (
            (election_dt.month, election_dt.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age_at_election >= minimum_age

if __name__ == '__main__':
    manager = VotingEligibilityManager("V12345", "1990-05-15")
    election_date = "2023-11-07"
    is_eligible = manager.is_eligible(election_date)
    print(is_eligible)