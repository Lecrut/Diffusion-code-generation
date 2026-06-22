class AccessGate:
    MIN_AGE = 18
    VALID_LEVELS = frozenset(['admin', 'premium', 'standard'])
    VALID_SUBSCRIPTIONS = frozenset(['active', 'expired'])

    @staticmethod
    def _validate_age(age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if age < AccessGate.MIN_AGE:
            return False
        return True

    @staticmethod
    def _validate_level(access_level):
        if access_level not in AccessGate.VALID_LEVELS:
            raise ValueError("Invalid access level")
        return True

    @staticmethod
    def _validate_subscription(subscription_status):
        if subscription_status not in AccessGate.VALID_SUBSCRIPTIONS:
            raise ValueError("Invalid subscription status")
        if subscription_status != 'active':
            return False
        return True

    @staticmethod
    def check_access(age, access_level, subscription_status):
        if not AccessGate._validate_age(age):
            return False
        if not AccessGate._validate_level(access_level):
            return False
        if not AccessGate._validate_subscription(subscription_status):
            return False
        if access_level == 'admin':
            return True
        if access_level == 'premium':
            return True
        if access_level == 'standard' and age >= 25:
            return True
        return False

if __name__ == '__main__':
    result = AccessGate.check_access(30, 'standard', 'active')
    print(result)