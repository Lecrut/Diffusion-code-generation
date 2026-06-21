def is_eligible_to_vote(age):
    return age >= 18

if __name__ == '__main__':
    age_1 = 17
    age_2 = 21
    print(is_eligible_to_vote(age_1))
    print(is_eligible_to_vote(age_2))