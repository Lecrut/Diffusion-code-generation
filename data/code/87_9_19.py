class UserAccessChecker:
    def __init__(self, is_active: bool, has_permission: bool):
        self.is_active = is_active
        self.has_permission = has_permission

    def can_proceed(self) -> bool:
        return self.is_active and self.has_permission

if __name__ == '__main__':
    user1 = UserAccessChecker(True, True)
    print(f"User 1 can proceed: {user1.can_proceed()}")

    user2 = UserAccessChecker(False, True)
    print(f"User 2 can proceed: {user2.can_proceed()}")