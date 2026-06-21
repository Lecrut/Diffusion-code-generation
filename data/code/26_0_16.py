ELIGIBILITY_STATUS = {
    'eligible': 18,
    'ineligible': 0
}

def get_voting_eligibility(age):
    status = 'ineligible'
    if age is not None and age >= ELIGIBILITY_STATUS['eligible']:
        status = 'eligible'
    return status == 'eligible'

if __name__ == '__main__':
    test_ages = [17, 18, 19, 65]
    for current_age in test_ages:
        print(get_voting_eligibility(current_age))