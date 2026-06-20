class AccessValidator:
    MIN_AGE = 18
    ACCESS_LEVEL = 'admin'
    
    @staticmethod
    def is_subscription_active(subscription):
        return subscription == 'active'

if __name__ == '__main__':
    user_age = 25
    user_access_level = 'admin'
    user_subscription = 'active'

    age_condition = user_age >= AccessValidator.MIN_AGE
    access_condition = user_access_level == AccessValidator.ACCESS_LEVEL
    subscription_condition = AccessValidator.is_subscription_active(user_subscription)

    if all([age_condition, access_condition, subscription_condition]):
        print("Access granted")
    else:
        print("Access denied")