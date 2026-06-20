MIN_AGE = 18
PERMISSION_GRANTED = 'yes'

def check_access(age, permission):
    return age >= MIN_AGE or permission == PERMISSION_GRANTED

if __name__ == '__main__':
    print(check_access(20, 'no'))
    print(check_access(15, 'yes'))