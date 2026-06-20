def check_access(age, permission):
    if age >= 18 or permission:
        return "Access granted"
    else:
        return "Access denied"

if __name__ == '__main__':
    print(check_access(20, False))
    print(check_access(17, True))
    print(check_access(15, True))