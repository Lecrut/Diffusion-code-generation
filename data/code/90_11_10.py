def check_access(age, permission):
    return age >= 18 or permission == 'yes'

if __name__ == '__main__':
    user_age = 25
    user_permission = 'no'
    access_granted = check_access(user_age, user_permission)
    print(access_granted)