def is_eligible_to_vote(age):
    if age < 0:
        return False
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    print(is_eligible_to_vote(17))
    print(is_eligible_to_vote(18))
    print(is_eligible_to_vote(21))
    print(is_eligible_to_vote(-1))