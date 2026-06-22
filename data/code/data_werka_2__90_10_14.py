def evaluate_access_request(age, permission_granted):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(permission_granted, bool):
        raise ValueError("permission_granted must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18 or permission_granted

def display_result(access_status):
    return "Access Granted" if access_status else "Access Denied"

if __name__ == '__main__':
    user_age = 16
    user_permission = True
    is_authorized = evaluate_access_request(user_age, user_permission)
    output_message = display_result(is_authorized)
    print(output_message)