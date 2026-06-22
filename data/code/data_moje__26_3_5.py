class Voter:
    def check_eligibility(self, age):
        if not isinstance(age, int):
            return False
        return age >= 18

if __name__ == '__main__':
    voter = Voter()
    print(voter.check_eligibility(20))
    print(voter.check_eligibility(15))