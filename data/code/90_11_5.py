def check_access(age, has_permission):
    if age >= 18 or has_permission:
        return "Access granted"
    else:
        return "Access denied"

if __name__ == '__main__':
    print(check_access(20, False))
    print(check_access(15, True))