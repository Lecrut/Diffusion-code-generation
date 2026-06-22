class VoterEligibility:
    def is_eligible(self, age):
        if not isinstance(age, int):
            return False
        return age >= 18

if __name__ == '__main__':
    voter = VoterEligibility()
    print(voter.is_eligible(20))
    print(voter.is_eligible(17))
    print(voter.is_eligible(18))
    print(voter.is_eligible(18.5))
    print(voter.is_eligible(-5))