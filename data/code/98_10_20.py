def check_access(age, access_level, is_subscriber):
    if age < 18:
        return False
    if access_level < 2:
        return False
    if not is_subscriber:
        return False
    return True

if __name__ == '__main__':
    age = 25
    access_level = 3
    is_subscriber = True
    result = check_access(age, access_level, is_subscriber)
    print(result)