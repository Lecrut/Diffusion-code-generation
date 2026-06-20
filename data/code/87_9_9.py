def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    sample_is_active = True
    sample_has_permission = False
    result = can_proceed(sample_is_active, sample_has_permission)
    print(f"User can proceed: {result}")