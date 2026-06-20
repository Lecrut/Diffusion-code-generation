def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission
if __name__ == '__main__':
    print(can_proceed(True, True))
    print(can_proceed(False, True))
    print(can_proceed(True, False))
    print(can_proceed(False, False))