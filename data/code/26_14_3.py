from enum import IntFlag
from dataclasses import dataclass

class StatusFlags(IntFlag):
    AGE_OK = 1
    CITIZEN_OK = 2
    DISFRANCHISED = 4

@dataclass(frozen=True)
class VoterStatus:
    age_valid: bool
    citizenship_valid: bool
    is_disenfranchised: bool

    def to_flags(self) -> int:
        flags = 0
        if self.age_valid:
            flags |= StatusFlags.AGE_OK
        if self.citizenship_valid:
            flags |= StatusFlags.CITIZEN_OK
        if self.is_disenfranchised:
            flags |= StatusFlags.DISFRANCHISED
        return flags

def check_voting_eligibility(flags: int) -> bool:
    has_age = (flags & StatusFlags.AGE_OK) != 0
    has_citizenship = (flags & StatusFlags.CITIZEN_OK) != 0
    is_disenfranchised = (flags & StatusFlags.DISFRANCHISED) != 0
    return has_age and has_citizenship and not is_disenfranchised

if __name__ == '__main__':
    sample_flags = StatusFlags.AGE_OK | StatusFlags.CITIZEN_OK
    result = check_voting_eligibility(sample_flags)
    print(result)

    sample_disenfranchised_flags = StatusFlags.AGE_OK | StatusFlags.CITIZEN_OK | StatusFlags.DISFRANCHISED
    result_disenfranchised = check_voting_eligibility(sample_disenfranchised_flags)
    print(result_disenfranchised)

    sample_no_age_flags = StatusFlags.CITIZEN_OK
    result_no_age = check_voting_eligibility(sample_no_age_flags)
    print(result_no_age)