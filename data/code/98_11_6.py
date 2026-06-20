def can_proceed(age, access_level, subscription_status):
    if age >= 18 and access_level == 'admin' and subscription_status:
        return True
    else:
        return False

if __name__ == '__main__':
    print(can_proceed(25, 'admin', True))