class VotingEligibility:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        if self.age < 18:
            return False
        return True

if __name__ == '__main__':
    voter1 = VotingEligibility(17)
    voter2 = VotingEligibility(18)
    voter3 = VotingEligibility(25)
    voter4 = VotingEligibility(19.5)
    print(voter1.is_eligible())
    print(voter2.is_eligible())
    print(voter3.is_eligible())
    print(voter4.is_eligible())