def is_eligible_to_vote(age):
    return age >= 18

if __name__ == '__main__':
    print(is_eligible_to_vote(17))
    print(is_eligible_to_vote(18))
    print(is_eligible_to_vote(21))