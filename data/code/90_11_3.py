def check_access(age, permission):
    return age >= 18 or permission == 'yes'

if __name__ == '__main__':
    print(check_access(20, 'no'))
    print(check_access(15, 'yes'))