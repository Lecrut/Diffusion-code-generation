def calculate_voting_eligibility(age, is_citizen, is_disenfranchised):
    age_flag = 1 if age >= 18 else 0
    citizen_flag = 1 if is_citizen else 0
    disenfranchised_flag = 1 if is_disenfranchised else 0
    
    status = (age_flag << 2) | (citizen_flag << 1) | disenfranchised_flag
    
    eligible = (status & 0b110) == 0b110
    
    return eligible

if __name__ == '__main__':
    age = 25
    is_citizen = True
    is_disenfranchised = False
    
    result = calculate_voting_eligibility(age, is_citizen, is_disenfranchised)
    print(result)