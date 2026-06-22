class VotingEligibility:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int) or isinstance(self.age, bool):
            return False
        return self.age >= 18

if __name__ == '__main__':
    voter1 = VotingEligibility(20)
    print(voter1.is_eligible())
    voter2 = VotingEligibility(17)
    print(voter2.is_eligible())
    voter3 = VotingEligibility(18)
    print(voter3.is_eligible())
    voter4 = VotingEligibility("20")
    print(voter4.is_eligible())
    voter5 = VotingEligibility(18.5)
    print(voter5.is_eligible())