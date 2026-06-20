def validate_age(age):
    return isinstance(age, int) and age >= 0

def validate_permission(permission):
    return permission.lower() in ['yes', 'no']

def check_access(age, permission):
    if not validate_age(age):
        raise ValueError("Invalid age")
    if not validate_permission(permission):
        raise ValueError("Invalid permission")
    return age >= 18 or permission == 'yes'

if __name__ == '__main__':
    print(check_access(20, 'no'))
    print(check_access(15, 'yes'))