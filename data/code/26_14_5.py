AGE_FLAG = 1
CITIZEN_FLAG = 2
DISENFRANCHISED_FLAG = 4

def check_voting_eligibility(status_flags: int, current_age: int, is_citizen: bool, is_disenfranchised: bool) -> bool:
    updated_flags = status_flags
    if current_age >= 18:
        updated_flags |= AGE_FLAG
    if is_citizen:
        updated_flags |= CITIZEN_FLAG
    if is_disenfranchised:
        updated_flags |= DISENFRANCHISED_FLAG
    
    has_age = (updated_flags & AGE_FLAG) != 0
    has_citizenship = (updated_flags & CITIZEN_FLAG) != 0
    is_barred = (updated_flags & DISENFRANCHISED_FLAG) != 0
    
    return has_age and has_citizenship and not is_barred

if __name__ == '__main__':
    sample_flags = 0
    age_1 = 20
    citizen_1 = True
    disenfranchised_1 = False
    result_1 = check_voting_eligibility(sample_flags, age_1, citizen_1, disenfranchised_1)
    print(result_1)
    
    sample_flags = 0
    age_2 = 16
    citizen_2 = True
    disenfranchised_2 = False
    result_2 = check_voting_eligibility(sample_flags, age_2, citizen_2, disenfranchised_2)
    print(result_2)
    
    sample_flags = 0
    age_3 = 25
    citizen_3 = True
    disenfranchised_3 = True
    result_3 = check_voting_eligibility(sample_flags, age_3, citizen_3, disenfranchised_3)
    print(result_3)
    
    sample_flags = 0
    age_4 = 30
    citizen_4 = False
    disenfranchised_4 = False
    result_4 = check_voting_eligibility(sample_flags, age_4, citizen_4, disenfranchised_4)
    print(result_4)