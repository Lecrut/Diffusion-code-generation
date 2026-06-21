def check_access(age, access_level, subscription_status):
    if age < 18:
        return False
    if access_level not in (1, 2, 3):
        return False
    if subscription_status != 'active':
        return False
    return True

if __name__ == '__main__':
    age = 25
    access_level = 2
    subscription_status = 'active'
    result = check_access(age, access_level, subscription_status)
    print(result)