MINIMUM_VOTING_AGE = 18

def can_vote(age):
    is_of_age = age > MINIMUM_VOTING_AGE
    return is_of_age

if __name__ == '__main__':
    test_ages = [17, 18, 19, 21, 65]
    results = []
    for a in test_ages:
        results.append(can_vote(a))
    print(results)