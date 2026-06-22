class Voter:
    def __init__(self, age):
        self.age = age

    def is_eligible(self):
        if not isinstance(self.age, int):
            return False
        return self.age >= 18

if __name__ == '__main__':
    voter1 = Voter(20)
    print(voter1.is_eligible())
    voter2 = Voter(17)
    print(voter2.is_eligible())
    voter3 = Voter(18)
    print(voter3.is_eligible())
    voter4 = Voter(18.5)
    print(voter4.is_eligible())
    voter5 = Voter(-5)
    print(voter5.is_eligible())