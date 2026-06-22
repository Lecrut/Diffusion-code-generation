def is_eligible_to_vote(age):
    return age >= 18

if __name__ == '__main__':
    sample_age_1 = 17
    sample_age_2 = 18
    sample_age_3 = 25
    print(is_eligible_to_vote(sample_age_1))
    print(is_eligible_to_vote(sample_age_2))
    print(is_eligible_to_vote(sample_age_3))