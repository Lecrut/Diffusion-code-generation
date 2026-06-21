class AccessController:
    def __init__(self, age, access_level, subscription_status):
        self.age = age
        self.access_level = access_level
        self.subscription_status = subscription_status

    def validate_age(self):
        return self.age >= 18

    def validate_level(self):
        valid_levels = ('admin', 'editor', 'viewer')
        if self.access_level not in valid_levels:
            raise ValueError("Invalid access level")
        return True

    def validate_subscription(self):
        if self.subscription_status != 'active':
            raise ValueError("Inactive subscription")
        return True

    def check_admin_access(self):
        if self.access_level == 'admin':
            return True
        return False

    def check_editor_access(self):
        if self.access_level == 'editor' and self.subscription_status == 'active':
            return True
        return False

    def check_viewer_access(self):
        if self.access_level == 'viewer' and self.age >= 21:
            return True
        return False

    def get_access_status(self):
        age_ok = self.validate_age()
        level_ok = self.validate_level()
        sub_ok = self.validate_subscription()
        if not (age_ok and level_ok and sub_ok):
            return False
        if self.check_admin_access():
            return True
        if self.check_editor_access():
            return True
        if self.check_viewer_access():
            return True
        return False

if __name__ == '__main__':
    controller = AccessController(25, 'editor', 'active')
    print(controller.get_access_status())
    print(controller.check_admin_access())
    print(controller.check_editor_access())