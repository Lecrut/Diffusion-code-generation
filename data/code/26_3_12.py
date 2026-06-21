class Voter:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        return self.age >= 18

if __name__ == '__main__':
    eligible_voter = Voter(20)
    ineligible_voter = Voter(16)
    print(eligible_voter.is_eligible())
    print(ineligible_voter.is_eligible())