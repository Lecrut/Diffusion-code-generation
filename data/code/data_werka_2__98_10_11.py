class AccessGate:
    def __init__(self, age, access_level, subscription_status):
        self.age = age
        self.access_level = access_level
        self.subscription_status = subscription_status

    def is_adult(self):
        return self.age >= 18

    def has_valid_level(self):
        return self.access_level in ('admin', 'user', 'guest')

    def is_subscribed(self):
        return self.subscription_status == 'active'

    def can_proceed(self):
        if not self.is_adult():
            return False
        if not self.has_valid_level():
            raise ValueError("Invalid access level")
        if not self.is_subscribed():
            return False
        if self.access_level == 'admin':
            return True
        if self.access_level == 'user' and self.is_subscribed():
            return True
        if self.access_level == 'guest' and self.age >= 21:
            return True
        return False

if __name__ == '__main__':
    gate = AccessGate(25, 'user', 'active')
    print(gate.can_proceed())
    print(gate.is_adult())
    print(gate.has_valid_level())
    print(gate.is_subscribed())