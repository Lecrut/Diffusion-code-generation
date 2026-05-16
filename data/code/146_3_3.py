class DecisionMaker:
    def is_eligible(self, age, has_permission, is_active):
        return (age >= 18 and has_permission and is_active) or (age >= 65)
if __name__ == '__main__':
    dm = DecisionMaker()
    user1_age = 25
    user1_permission = True
    user1_active = True
    result1 = dm.is_eligible(user1_age, user1_permission, user1_active)
    print(f"User 1 Eligibility: {result1}")
    user2_age = 70
    user2_permission = False
    user2_active = True
    result2 = dm.is_eligible(user2_age, user2_permission, user2_active)
    print(f"User 2 Eligibility: {result2}")
    user3_age = 16
    user3_permission = True
    user3_active = True
    result3 = dm.is_eligible(user3_age, user3_permission, user3_active)
    print(f"User 3 Eligibility: {result3}")