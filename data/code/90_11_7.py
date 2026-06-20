class AccessControl:
    def __init__(self):
        self.age = None
        self.permission = None

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.age = age
        else:
            raise ValueError("Age must be a non-negative integer")

    def set_permission(self, permission):
        if isinstance(permission, str) and permission.lower() in ['yes', 'no']:
            self.permission = permission.lower()
        else:
            raise ValueError("Permission must be 'yes' or 'no'")

    def check_access(self):
        return self.age >= 18 or self.permission == 'yes'

if __name__ == '__main__':
    access_control = AccessControl()
    access_control.set_age(20)
    access_control.set_permission('no')
    print(access_control.check_access())

    access_control.set_age(15)
    access_control.set_permission('yes')
    print(access_control.check_access())