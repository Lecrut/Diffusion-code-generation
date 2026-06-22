def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        return {'eligible': False, 'message': 'Invalid input: Age must be a number.'}
    if age < 0:
        return {'eligible': False, 'message': 'Invalid input: Age cannot be negative.'}
    if age < 18:
        return {'eligible': False, 'message': 'Not eligible: Must be 18 or older.'}
    return {'eligible': True, 'message': 'Eligible to vote.'}
if __name__ == '__main__':
    test_ages = [20, 17, -5, 18.5, 0, 'teen']
    for age in test_ages:
        result = check_voting_eligibility(age)
        print(f"Age {age!r}: {result['message']}")