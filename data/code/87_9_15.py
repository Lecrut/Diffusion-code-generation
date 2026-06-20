class UserPermission:

    def can_proceed(self, is_active: bool, has_permission: bool) -> bool:
        return is_active and has_permission
if __name__ == '__main__':
    user = UserPermission()
    print(user.can_proceed(True, False))
    print(user.can_proceed(False, True))
    print(user.can_proceed(True, True))
    print(user.can_proceed(False, False))