def check_access(age, access_level, is_subscriber):
    if age < 18:
        return False
    if access_level not in (1, 2, 3):
        return False
    if not is_subscriber:
        return False
    return True

if __name__ == '__main__':
    result = check_access(25, 2, True)
    print(result)