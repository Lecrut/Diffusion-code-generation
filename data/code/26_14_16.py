from enum import IntFlag
from typing import NamedTuple

class VotingStatus(IntFlag):
    AGE = 1
    CITIZENSHIP = 2
    DISFRANCHISED = 4

class VotingResult(NamedTuple):
    eligible: bool
    reasons: list

def calculate_eligibility(age_flag: int, citizenship_flag: int, disenfranchised_flag: int) -> VotingResult:
    flags = (age_flag & VotingStatus.AGE) | (citizenship_flag & VotingStatus.CITIZENSHIP)
    if disenfranchised_flag & VotingStatus.DISFRANCHISED:
        return VotingResult(eligible=False, reasons=["Disenfranchised status active"])
    
    if (flags & VotingStatus.AGE) and (flags & VotingStatus.CITIZENSHIP):
        return VotingResult(eligible=True, reasons=[])
    
    reasons = []
    if not (flags & VotingStatus.AGE):
        reasons.append("Age requirement not met")
    if not (flags & VotingStatus.CITIZENSHIP):
        reasons.append("Citizenship requirement not met")
    
    return VotingResult(eligible=False, reasons=reasons)

if __name__ == '__main__':
    test_cases = [
        (VotingStatus.AGE.value, VotingStatus.CITIZENSHIP.value, 0),
        (0, VotingStatus.CITIZENSHIP.value, 0),
        (VotingStatus.AGE.value, 0, 0),
        (VotingStatus.AGE.value, VotingStatus.CITIZENSHIP.value, VotingStatus.DISFRANCHISED.value),
        (VotingStatus.AGE.value, 0, VotingStatus.DISFRANCHISED.value)
    ]
    
    for age, citizenship, disenfranchised in test_cases:
        result = calculate_eligibility(age, citizenship, disenfranchised)
        print(result)