class AccessController:
    def __init__(self, age, has_permission):
        if not isinstance(age, int) or isinstance(age, bool):
            raise ValueError("age must be an integer")
        if not isinstance(has_permission, bool):
            raise ValueError("has_permission must be a boolean")
        if age < 0:
            raise ValueError("age cannot be negative")
        self.age = age
        self.has_permission = has_permission

    def can_access(self):
        return self.age >= 18 or self.has_permission

    def get_status(self):
        if self.can_access():
            return "Granted"
        return "Denied"

if __name__ == '__main__':
    controller = AccessController(17, True)
    print(controller.can_access())
    print(controller.get_status())