MINIMUM_AGE = 18

def can_vote(age):
    if age is None:
        return False
    return age > MINIMUM_AGE

if __name__ == '__main__':
    ages_to_check = [16, 18, 19, None]
    for a in ages_to_check:
        print(can_vote(a))