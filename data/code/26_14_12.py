import enum
import typing

class VotingStatus(enum.IntFlag):
    AGE = 1
    CITIZENSHIP = 2
    DISENFRANCHISED = 4

def check_voting_eligibility(age: bool, is_citizen: bool, is_disenfranchised: bool) -> typing.Tuple[bool, VotingStatus]:
    flags = 0
    if age:
        flags |= VotingStatus.AGE
    if is_citizen:
        flags |= VotingStatus.CITIZENSHIP
    if is_disenfranchised:
        flags |= VotingStatus.DISENFRANCHISED
    
    has_age = (flags & VotingStatus.AGE) != 0
    has_citizenship = (flags & VotingStatus.CITIZENSHIP) != 0
    is_disqualified = (flags & VotingStatus.DISENFRANCHISED) != 0
    
    if not has_age or not has_citizenship or is_disqualified:
        return False, flags
    
    return True, flags

if __name__ == '__main__':
    sample_age_true = True
    sample_citizen_true = True
    sample_disenfranchised_false = False
    
    result_eligible, flags_eligible = check_voting_eligibility(sample_age_true, sample_citizen_true, sample_disenfranchised_false)
    print(result_eligible)
    print(flags_eligible)
    
    sample_age_false = False
    sample_citizen_true_2 = True
    sample_disenfranchised_false_2 = False
    
    result_ineligible_age, flags_ineligible_age = check_voting_eligibility(sample_age_false, sample_citizen_true_2, sample_disenfranchised_false_2)
    print(result_ineligible_age)
    print(flags_ineligible_age)
    
    sample_age_true_3 = True
    sample_citizen_false = False
    sample_disenfranchised_false_3 = False
    
    result_ineligible_cit, flags_ineligible_cit = check_voting_eligibility(sample_age_true_3, sample_citizen_false, sample_disenfranchised_false_3)
    print(result_ineligible_cit)
    print(flags_ineligible_cit)
    
    sample_age_true_4 = True
    sample_citizen_true_4 = True
    sample_disenfranchised_true = True
    
    result_disqualified, flags_disqualified = check_voting_eligibility(sample_age_true_4, sample_citizen_true_4, sample_disenfranchised_true)
    print(result_disqualified)
    print(flags_disqualified)