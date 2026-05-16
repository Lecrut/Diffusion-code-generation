class DecisionMaker:
    def is_eligible(self, age, has_permission, is_active):
        if age >= 18 and has_permission and is_active:
            return True
        else:
            return False
if __name__ == '__main__':
    dm = DecisionMaker()
    age1 = 25
    permission1 = True
    active1 = True
    result1 = dm.is_eligible(age1, permission1, active1)
    print(f"User 1 eligibility: {result1}")
    age2 = 16
    permission2 = True
    active2 = True
    result2 = dm.is_eligible(age2, permission2, active2)
    print(f"User 2 eligibility: {result2}")
    age3 = 30
    permission3 = False
    active3 = True
    result3 = dm.is_eligible(age3, permission3, active3)
    print(f"User 3 eligibility: {result3}")
    age4 = 40
    permission4 = True
    active4 = False
    result4 = dm.is_eligible(age4, permission4, active4)
    print(f"User 4 eligibility: {result4}")