def can_vote(age):
    return age >= 18

if __name__ == '__main__':
    print(can_vote(18))
    print(can_vote(17))
    print(can_vote(21))