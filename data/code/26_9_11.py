def can_vote(age):
    return age > 18

if __name__ == '__main__':
    sample_age = 20
    result = can_vote(sample_age)
    print(result)