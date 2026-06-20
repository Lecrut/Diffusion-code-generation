def check_access(age, has_permission):
    if age >= 18 or has_permission:
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_access(20, False))
    print(check_access(15, True))
    print(check_access(17, True))