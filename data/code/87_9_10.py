def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    active_status = True
    permission_status = False
    result1 = can_proceed(active_status, permission_status)
    print(f"Can proceed with active status {active_status} and permission {permission_status}: {result1}")
    
    active_status = False
    permission_status = True
    result2 = can_proceed(active_status, permission_status)
    print(f"Can proceed with active status {active_status} and permission {permission_status}: {result2}")
    
    active_status = True
    permission_status = True
    result3 = can_proceed(active_status, permission_status)
    print(f"Can proceed with active status {active_status} and permission {permission_status}: {result3}")