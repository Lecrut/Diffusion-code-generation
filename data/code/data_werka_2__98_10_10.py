def check_access(age, access_level, subscription_status):
    if age < 18:
        return False
    if access_level not in (1, 2, 3):
        return False
    if subscription_status != 'active':
        return False
    return True

if __name__ == '__main__':
    result = check_access(25, 2, 'active')
    print(result)