def check_voter_eligibility(voter_attributes: dict[str, int]) -> bool:
    age = voter_attributes.get('age')
    citizenship_years = voter_attributes.get('citizenship_years')
    
    if age is None or citizenship_years is None:
        raise ValueError("Missing required attributes: 'age' and 'citizenship_years'")
    
    if not isinstance(age, int) or not isinstance(citizenship_years, int):
        raise TypeError("Attributes must be integers")
    
    if age < 18:
        return False
    
    if citizenship_years < 1:
        return False
    
    return True

if __name__ == '__main__':
    sample_voter = {'age': 25, 'citizenship_years': 5}
    print(check_voter_eligibility(sample_voter))
    
    ineligible_voter = {'age': 16, 'citizenship_years': 10}
    print(check_voter_eligibility(ineligible_voter))
    
    new_citizen = {'age': 30, 'citizenship_years': 0}
    print(check_voter_eligibility(new_citizen))