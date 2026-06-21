def is_voting_eligible(age):
    if age < 0:
        return False
    return age >= 18

if __name__ == '__main__':
    test_ages = [17, 18, 25, 100, -5]
    for age in test_ages:
        print(is_voting_eligible(age))