class DecisionMaker:
    def is_eligible(self, age, has_permission, is_active):
        if age >= 18 and has_permission and is_active:
            return True
        return False
if __name__ == '__main__':
    dm = DecisionMaker()
    user_age = 25
    permission_status = True
    account_active = False
    eligibility = dm.is_eligible(user_age, permission_status, account_active)
    print(f"User Age: {user_age}")
    print(f"Has Permission: {permission_status}")
    print(f"Account Active: {account_active}")
    print(f"Eligibility: {eligibility}")