def can_vote(age):
    return age > 17

if __name__ == '__main__':
    print(can_vote(16))
    print(can_vote(18))
    print(can_vote(21))