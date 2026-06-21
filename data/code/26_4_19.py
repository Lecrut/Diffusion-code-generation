def check_voting_status(age, voting_age=18):
    if age >= voting_age:
        return True
    return False

if __name__ == '__main__':
    sample_age_1 = 17
    sample_age_2 = 20
    sample_age_3 = 18
    result_1 = check_voting_status(sample_age_1)
    result_2 = check_voting_status(sample_age_2)
    result_3 = check_voting_status(sample_age_3, 21)
    print(result_1)
    print(result_2)
    print(result_3)