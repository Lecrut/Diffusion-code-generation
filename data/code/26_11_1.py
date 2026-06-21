import time
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Tuple

@dataclass
class VoterRecord:
    name: str
    birth_date: datetime
    citizen: bool
    registered: bool
    id_number: str
    disqualified_until: Optional[datetime] = None

class VotingEligibilityManager:
    MIN_VOTING_AGE = 18
    DISQUALIFICATION_TYPES = {
        'felony': 10,
        'misdemeanor': 2
    }

    def __init__(self):
        self._records: List[VoterRecord] = []
        self._cache: dict = {}
        self._cache_timeout: float = 0.0

    def register_voter(self, name: str, birth_date: datetime, is_citizen: bool, is_registered: bool, 
                     voter_id: str, felony: bool = False, misdemeanor: bool = False) -> None:
        disqualified_until = None
        if felony:
            disqualified_until = datetime.now().replace(year=datetime.now().year + 10)
        elif misdemeanor:
            disqualified_until = datetime.now().replace(year=datetime.now().year + 2)
        
        record = VoterRecord(
            name=name,
            birth_date=birth_date,
            citizen=is_citizen,
            registered=is_registered,
            id_number=voter_id,
            disqualified_until=disqualified_until
        )
        self._records.append(record)
        self._clear_cache()

    def _clear_cache(self) -> None:
        self._cache.clear()
        self._cache_timeout = 0.0

    def _calculate_age(self, birth_date: datetime) -> int:
        today = datetime.now()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def check_eligibility(self, voter_id: str) -> Tuple[bool, str]:
        now = datetime.now()
        cache_key = f"{voter_id}_{int(now.timestamp())}"
        
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        record = next((r for r in self._records if r.id_number == voter_id), None)
        
        if not record:
            return False, "Voter not found"
        
        age = self._calculate_age(record.birth_date)
        
        if age < self.MIN_VOTING_AGE:
            return False, "Insufficient age"
        
        if not record.citizen:
            return False, "Not a citizen"
        
        if not record.registered:
            return False, "Not registered"
        
        if record.disqualified_until and now < record.disqualified_until:
            years_left = record.disqualified_until.year - now.year
            return False, f"Disqualified for {years_left} more years"
        
        return True, "Eligible"

    def get_all_eligible_voters(self) -> List[str]:
        eligible_ids = []
        now = datetime.now()
        
        for record in self._records:
            if record.citizen and record.registered:
                age = self._calculate_age(record.birth_date)
                if age >= self.MIN_VOTING_AGE:
                    if not record.disqualified_until or now > record.disqualified_until:
                        eligible_ids.append(record.id_number)
        return eligible_ids

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    
    manager.register_voter(
        name="Alice Smith",
        birth_date=datetime(1990, 5, 15),
        is_citizen=True,
        is_registered=True,
        voter_id="V001"
    )
    
    manager.register_voter(
        name="Bob Jones",
        birth_date=datetime(2010, 3, 20),
        is_citizen=True,
        is_registered=True,
        voter_id="V002"
    )
    
    manager.register_voter(
        name="Charlie Brown",
        birth_date=datetime(1985, 8, 10),
        is_citizen=False,
        is_registered=True,
        voter_id="V003"
    )
    
    manager.register_voter(
        name="Diana Prince",
        birth_date=datetime(1975, 12, 1),
        is_citizen=True,
        is_registered=True,
        voter_id="V004",
        felony=True
    )
    
    print(manager.check_eligibility("V001"))
    print(manager.check_eligibility("V002"))
    print(manager.check_eligibility("V003"))
    print(manager.check_eligibility("V004"))
    print(manager.get_all_eligible_voters())