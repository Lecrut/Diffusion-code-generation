def can_vote(age):
    return age > 18

if __name__ == '__main__':
    test_age_1 = 17
    test_age_2 = 18
    test_age_3 = 19
    print(can_vote(test_age_1))
    print(can_vote(test_age_2))
    print(can_vote(test_age_3))