class VotingEligibility:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        return self.age >= 18

if __name__ == '__main__':
    test_cases = [17, 18, 25, '20', 100]
    for age in test_cases:
        voter = VotingEligibility(age)
        print(f"Age {age}: {voter.is_eligible()}")