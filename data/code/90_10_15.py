class Gatekeeper:
    def __init__(self, user_age, has_permission):
        if not isinstance(user_age, int) or isinstance(user_age, bool):
            raise ValueError("user_age must be an integer")
        if not isinstance(has_permission, bool):
            raise ValueError("has_permission must be a boolean")
        if user_age < 0:
            raise ValueError("user_age cannot be negative")
        self.user_age = user_age
        self.has_permission = has_permission

    def check_access(self):
        return self.user_age >= 18 or self.has_permission

    def get_reason(self):
        if self.user_age >= 18:
            return "age"
        if self.has_permission:
            return "permission"
        return "none"

if __name__ == '__main__':
    gate = Gatekeeper(17, False)
    print(gate.check_access())
    print(gate.get_reason())
    gate2 = Gatekeeper(17, True)
    print(gate2.check_access())
    print(gate2.get_reason())