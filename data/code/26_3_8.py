class VotingEligibility:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        return self.age >= 18

if __name__ == '__main__':
    sample_ages = [17, 18, 19, 25, '18', 100]
    for age in sample_ages:
        voter = VotingEligibility(age)
        print(voter.is_eligible())