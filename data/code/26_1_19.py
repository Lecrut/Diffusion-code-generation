MIN_VOTING_AGE = 18

def is_eligible_to_vote(age: int) -> bool:
    if not isinstance(age, int):
        return False
    if age < 0:
        return False
    return age >= MIN_VOTING_AGE

def check_voting_status(age: int) -> str:
    if not isinstance(age, int):
        return "Invalid input"
    if age < 0:
        return "Invalid input"
    
    if is_eligible_to_vote(age):
        return "Eligible"
    else:
        return "Not eligible"

if __name__ == '__main__':
    sample_ages = [20, 17, -5, 0, 18, 65]
    for age in sample_ages:
        print(check_voting_status(age))