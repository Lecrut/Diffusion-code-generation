class Voter:
    def is_eligible(self, age):
        return isinstance(age, int) and not isinstance(age, bool) and age >= 18

if __name__ == '__main__':
    voter = Voter()
    print(voter.is_eligible(18))
    print(voter.is_eligible(17))
    print(voter.is_eligible(21))
    print(voter.is_eligible(18.5))
    print(voter.is_eligible(True))