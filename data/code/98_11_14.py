class UserAccessValidator:
    def __init__(self, age, access_level, subscription_status):
        self.age = age
        self.access_level = access_level
        self.subscription_status = subscription_status

    def is_allowed(self):
        conditions = [
            self.is_adult,
            self.has_high_access_level,
            self.is_subscribed
        ]
        return all(condition() for condition in conditions)

    def is_adult(self):
        return self.age >= 18

    def has_high_access_level(self):
        return self.access_level >= 3

    def is_subscribed(self):
        return self.subscription_status == "active"

if __name__ == '__main__':
    sample_user = UserAccessValidator(age=25, access_level=4, subscription_status="active")
    print(sample_user.is_allowed())