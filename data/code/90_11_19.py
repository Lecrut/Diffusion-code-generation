def check_access(age, permission):
    if not isinstance(age, int) or age < 0:
        raise ValueError('Age must be a non-negative integer')
    if permission not in ['yes', 'no']:
        raise ValueError("Permission must be either 'yes' or 'no'")
    return age >= 18 or permission == 'yes'
if __name__ == '__main__':
    try:
        print(check_access(20, 'no'))
        print(check_access(15, 'yes'))
        print(check_access(-5, 'yes'))
    except ValueError as e:
        print(e)