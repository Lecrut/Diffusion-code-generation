from typing import Tuple

AGE_FLAG = 1
CITIZENSHIP_FLAG = 2
DISENFRANCHISED_FLAG = 4

def check_voting_eligibility(status_flags: int) -> bool:
    has_age = (status_flags & AGE_FLAG) != 0
    is_citizen = (status_flags & CITIZENSHIP_FLAG) != 0
    is_disenfranchised = (status_flags & DISENFRANCHISED_FLAG) != 0
    
    if is_disenfranchised:
        return False
    
    return has_age and is_citizen

def combine_status_flags(is_age_qualified: bool, is_citizen: bool, is_disenfranchised: bool) -> int:
    flags = 0
    if is_age_qualified:
        flags |= AGE_FLAG
    if is_citizen:
        flags |= CITIZENSHIP_FLAG
    if is_disenfranchised:
        flags |= DISENFRANCHISED_FLAG
    return flags

if __name__ == '__main__':
    test_cases: list[Tuple[bool, bool, bool]] = [
        (True, True, False),
        (False, True, False),
        (True, False, False),
        (True, True, True),
        (False, False, True),
    ]
    
    for age, citizen, disenfranchised in test_cases:
        flags = combine_status_flags(age, citizen, disenfranchised)
        eligible = check_voting_eligibility(flags)
        print(f"Flags: {flags}, Age: {age}, Citizen: {citizen}, Disenfranchised: {disenfranchised} -> Eligible: {eligible}")