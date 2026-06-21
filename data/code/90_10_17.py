ACCESS_THRESHOLD = 21
PERMISSION_MULTIPLIER = 2

def evaluate_access_request(age, permission_level):
    if not isinstance(age, (int, float)):
        raise ValueError("age must be numeric")
    if not isinstance(permission_level, (int, float)):
        raise ValueError("permission_level must be numeric")
    if age < 0:
        raise ValueError("age cannot be negative")
    if permission_level < 0:
        raise ValueError("permission_level cannot be negative")
    weighted_age = age + (permission_level * PERMISSION_MULTIPLIER)
    return weighted_age >= ACCESS_THRESHOLD

if __name__ == '__main__':
    user_age = 16
    user_permission = 3
    access_granted = evaluate_access_request(user_age, user_permission)
    print(access_granted)