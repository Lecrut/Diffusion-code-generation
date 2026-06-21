def can_vote(age, threshold=18):
    return age >= threshold

if __name__ == '__main__':
    print(can_vote(20))
    print(can_vote(16))
    print(can_vote(18))
    print(can_vote(17))