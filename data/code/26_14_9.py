from dataclasses import dataclass
from typing import Final
FLAG_AGE: Final[int] = 1
FLAG_CITIZENSHIP: Final[int] = 2
FLAG_DISFRANCHISED: Final[int] = 4

@dataclass(frozen=True)
class VotingStatus:
    is_18: bool
    is_citizen: bool
    is_disenfranchised: bool

    def to_flags(self) -> int:
        flags = 0
        if self.is_18:
            flags |= FLAG_AGE
        if self.is_citizen:
            flags |= FLAG_CITIZENSHIP
        if self.is_disenfranchised:
            flags |= FLAG_DISFRANCHISED
        return flags

    @classmethod
    def from_flags(cls, flags: int) -> 'VotingStatus':
        return cls(is_18=bool(flags & FLAG_AGE), is_citizen=bool(flags & FLAG_CITIZENSHIP), is_disenfranchised=bool(flags & FLAG_DISFRANCHISED))

def check_eligibility(flags: int) -> bool:
    has_age = flags & FLAG_AGE
    has_citizen = flags & FLAG_CITIZENSHIP
    is_disenfranchised = flags & FLAG_DISFRANCHISED
    if not has_age or not has_citizen:
        return False
    if is_disenfranchised:
        return False
    return True

def calculate_eligibility(is_18: bool, is_citizen: bool, is_disenfranchised: bool) -> bool:
    status = VotingStatus(is_18=is_18, is_citizen=is_citizen, is_disenfranchised=is_disenfranchised)
    flags = status.to_flags()
    return check_eligibility(flags)
if __name__ == '__main__':
    sample_cases = [(True, True, False), (True, False, False), (False, True, False), (True, True, True), (False, False, True)]
    for is_18, is_citizen, is_disenfranchised in sample_cases:
        result = calculate_eligibility(is_18, is_citizen, is_disenfranchised)
        print(f'Eligible (Age:{is_18}, Citizen:{is_citizen}, Dis:{is_disenfranchised}): {result}')