def check_access(age, permission):
    if age >= 18 or permission == "yes":
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_access(20, "no"))
    print(check_access(15, "yes"))
    print(check_access(17, "yes"))