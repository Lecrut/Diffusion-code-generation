class AccessValidator:
    MIN_AGE = 18
    ACCESS_LEVEL = "admin"
    ACTIVE_SUBSCRIPTION = True

    @staticmethod
    def validate_age(age):
        return age >= AccessValidator.MIN_AGE

    @staticmethod
    def validate_access_level(level):
        return level == AccessValidator.ACCESS_LEVEL

    @staticmethod
    def validate_subscription(subscription):
        return subscription == AccessValidator.ACTIVE_SUBSCRIPTION

    def check_all_conditions(self, user_age, access_level, subscription_status):
        age_valid = self.validate_age(user_age)
        access_valid = self.validate_access_level(access_level)
        subscription_valid = self.validate_subscription(subscription_status)
        return age_valid and access_valid and subscription_valid

if __name__ == '__main__':
    validator = AccessValidator()
    user_data = {
        'age': 25,
        'access_level': "admin",
        'subscription_status': True
    }
    result = validator.check_all_conditions(user_data['age'], user_data['access_level'], user_data['subscription_status'])
    print(result)