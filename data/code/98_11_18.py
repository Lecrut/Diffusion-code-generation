def can_proceed(age, access_level, subscription_status):
    return age >= 18 and access_level == 'admin' and subscription_status

if __name__ == '__main__':
    print(can_proceed(25, 'admin', True))
    print(can_proceed(17, 'user', False))