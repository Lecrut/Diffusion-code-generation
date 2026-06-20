class AccessValidator:
    def __init__(self, age, access_level, subscription_active):
        self.age = age
        self.access_level = access_level
        self.subscription_active = subscription_active

    def validate_access(self):
        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError("Age must be a non-negative integer.")
        if not isinstance(self.access_level, str) or self.access_level not in ['admin', 'user']:
            raise ValueError("Access level must be either 'admin' or 'user'.")
        if not isinstance(self.subscription_active, bool):
            raise ValueError("Subscription status must be a boolean.")

        required_age = 18
        required_access_level = 'admin'
        subscription_required = True

        if self.age < required_age:
            return False
        if self.access_level != required_access_level and subscription_required and not self.subscription_active:
            return False

        return True

if __name__ == '__main__':
    validator = AccessValidator(age=25, access_level='user', subscription_active=True)
    print(validator.validate_access())