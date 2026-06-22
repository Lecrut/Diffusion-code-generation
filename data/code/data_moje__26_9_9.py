VOTING_AGE_THRESHOLD = 18

def check_voting_eligibility(age):
    is_of_age = age > VOTING_AGE_THRESHOLD
    return is_of_age

class VoterStatus:
    def __init__(self, age):
        self.age = age

    def get_eligibility(self):
        return check_voting_eligibility(self.age)

if __name__ == '__main__':
    test_ages = [17, 18, 19, 45]
    for age in test_ages:
        status = VoterStatus(age)
        print(status.get_eligibility())