class UserEligibilityChecker:
    def __init__(self):
        self.eligible_users = set()

    @staticmethod
    def check_eligibility(user_data):
        eligibility_checker = UserEligibilityChecker()
        return list(eligibility_checker._check_user_eligibility(user_data))

    def _check_user_eligibility(self, user_data):
        for user in user_data:
            if self._is_user_eligible(user):
                self.eligible_users.add(user['name'])
                yield user

    def _is_user_eligible(self, user):
        return (user.get('age', 0) >= 18 and
                user.get('is_member', False) and
                user.get('total_spent', 0) > 100)

if __name__ == '__main__':
    users = [
        {'name': 'Alice', 'age': 22, 'is_member': True, 'total_spent': 600},
        {'name': 'Bob', 'age': 30, 'is_member': True, 'total_spent': 1200},
        {'name': 'Charlie', 'age': 45, 'is_member': False, 'total_spent': 500},
        {'name': 'David', 'age': 20, 'is_member': True, 'total_spent': 50},
        {'name': 'Eve', 'age': 35, 'is_member': True, 'total_spent': 150}
    ]

    eligible_users = UserEligibilityChecker.check_eligibility(users)
    for user in eligible_users:
        print(f"User: {user['name']}, Eligible: Yes")