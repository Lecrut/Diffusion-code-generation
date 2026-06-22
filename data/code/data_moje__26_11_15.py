import time
from typing import List, Optional

class VotingRecordManager:
    MIN_AGE = 18
    MAX_AGE = 120

    def __init__(self) -> None:
        self._records: List[dict] = []

    def add_record(self, name: str, age: int, eligible: bool) -> None:
        if not isinstance(age, int) or age < self.MIN_AGE or age > self.MAX_AGE:
            return
        if age < self.MIN_AGE:
            is_eligible = False
        elif age > self.MAX_AGE:
            is_eligible = False
        else:
            is_eligible = eligible
        record = {'name': name, 'age': age, 'eligible': is_eligible, 'timestamp': time.time()}
        self._records.append(record)

    def check_eligibility(self, age: int) -> bool:
        if not isinstance(age, int):
            return False
        if age < self.MIN_AGE:
            return False
        if age > self.MAX_AGE:
            return False
        return True

    def get_eligible_voters(self) -> List[str]:
        eligible_names = []
        for record in self._records:
            if record['eligible']:
                eligible_names.append(record['name'])
        return eligible_names

    def get_voter_count(self) -> int:
        return len(self._records)

    def get_eligible_count(self) -> int:
        count = 0
        for record in self._records:
            if record['eligible']:
                count += 1
        return count
if __name__ == '__main__':
    manager = VotingRecordManager()
    manager.add_record('Alice', 25, True)
    manager.add_record('Bob', 16, False)
    manager.add_record('Charlie', 30, True)
    manager.add_record('Diana', 17, False)
    manager.add_record('Eve', 20, True)
    eligibility_status_alice = manager.check_eligibility(25)
    eligibility_status_bob = manager.check_eligibility(16)
    eligible_voters = manager.get_eligible_voters()
    total_voters = manager.get_voter_count()
    eligible_voter_count = manager.get_eligible_count()
    print(f'Alice eligible: {eligibility_status_alice}')
    print(f'Bob eligible: {eligibility_status_bob}')
    print(f'Eligible voters: {eligible_voters}')
    print(f'Total voters: {total_voters}')
    print(f'Eligible voter count: {eligible_voter_count}')