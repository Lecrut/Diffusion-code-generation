class AccessGate:
    MIN_AGE = 18
    VALID_LEVELS = ('admin', 'editor', 'viewer')
    ACTIVE_SUB = 'active'

    def __init__(self, age, access_level, subscription_status):
        self.age = age
        self.access_level = access_level
        self.subscription_status = subscription_status

    def validate_inputs(self):
        if not isinstance(self.age, int):
            raise ValueError("Age must be an integer")
        if self.age < self.MIN_AGE:
            raise ValueError("Age must be at least 18")
        if self.access_level not in self.VALID_LEVELS:
            raise ValueError("Invalid access level")
        if self.subscription_status != self.ACTIVE_SUB:
            raise ValueError("Subscription must be active")

    def check_permissions(self):
        self.validate_inputs()
        if self.access_level == 'admin':
            return True
        if self.access_level == 'editor':
            return True
        if self.access_level == 'viewer' and self.age >= 21:
            return True
        return False

if __name__ == '__main__':
    gate = AccessGate(25, 'editor', 'active')
    result = gate.check_permissions()
    print(result)