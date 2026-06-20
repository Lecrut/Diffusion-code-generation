MIN_AGE = 18
ACCESS_LEVEL = 3
SUBSCRIPTION_STATUS = True

def check_conditions(age, access_level, subscription_status):
    conditions = [
        age >= MIN_AGE,
        access_level >= ACCESS_LEVEL,
        subscription_status
    ]
    return all(conditions)

if __name__ == '__main__':
    sample_age = 25
    sample_access_level = 4
    sample_subscription_status = True

    result = check_conditions(sample_age, sample_access_level, sample_subscription_status)
    print(result)