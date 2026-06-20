class UserAccessChecker:
    @staticmethod
    def can_proceed(is_active: bool, has_permission: bool) -> bool:
        return is_active and has_permission

if __name__ == '__main__':
    access_checker = UserAccessChecker()
    result1 = access_checker.can_proceed(True, False)
    print(f"Can proceed (True, False): {result1}")
    result2 = access_checker.can_proceed(False, True)
    print(f"Can proceed (False, True): {result2}")
    result3 = access_checker.can_proceed(True, True)
    print(f"Can proceed (True, True): {result3}")
    result4 = access_checker.can_proceed(False, False)
    print(f"Can proceed (False, False): {result4}")