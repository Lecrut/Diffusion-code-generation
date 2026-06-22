from dataclasses import dataclass
from enum import IntFlag
import sys

class StatusFlags(IntFlag):
    AGE_OK = 1
    CITIZEN_OK = 2
    DISENFRANCHISED = 4

@dataclass(frozen=True)
class VoterStatus:
    age: int
    is_citizen: bool
    is_disenfranchised: bool

    def to_bits(self) -> int:
        bits = 0
        if self.age >= 18:
            bits |= StatusFlags.AGE_OK
        if self.is_citizen:
            bits |= StatusFlags.CITIZEN_OK
        if self.is_disenfranchised:
            bits |= StatusFlags.DISENFRANCHISED
        return bits

def check_eligibility(age: int, is_citizen: bool, is_disenfranchised: bool) -> bool:
    bits = 0
    if age >= 18:
        bits |= StatusFlags.AGE_OK
    if is_citizen:
        bits |= StatusFlags.CITIZEN_OK
    if is_disenfranchised:
        bits |= StatusFlags.DISENFRANCHISED
    eligible_flags = StatusFlags.AGE_OK | StatusFlags.CITIZEN_OK
    is_eligible = bits & eligible_flags == eligible_flags
    is_disqualified = bits & StatusFlags.DISENFRANCHISED != 0
    return is_eligible and (not is_disqualified)
if __name__ == '__main__':
    test_cases = [VoterStatus(20, True, False), VoterStatus(17, True, False), VoterStatus(25, False, False), VoterStatus(30, True, True), VoterStatus(45, True, False)]
    for case in test_cases:
        result = check_eligibility(case.age, case.is_citizen, case.is_disenfranchised)
        print(f'Age:{case.age} Citizen:{case.is_citizen} Disenfranchised:{case.is_disenfranchised} -> Eligible:{result}')