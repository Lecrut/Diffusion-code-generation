class ResourceGate:
    MIN_AGE = 18
    DENIED_STATUS = "Access Denied"
    GRANTED_STATUS = "Access Granted"

    @staticmethod
    def validate_inputs(age, has_permission):
        if not isinstance(age, int) or isinstance(age, bool):
            raise ValueError("age must be an integer")
        if not isinstance(has_permission, bool):
            raise ValueError("has_permission must be a boolean")
        if age < 0:
            raise ValueError("age cannot be negative")
        return True

    def __init__(self, age, has_permission):
        self.validate_inputs(age, has_permission)
        self.age = age
        self.has_permission = has_permission

    def check_access(self):
        return self.age >= self.MIN_AGE or self.has_permission

    def get_result_string(self):
        if self.check_access():
            return self.GRANTED_STATUS
        return self.DENIED_STATUS

if __name__ == '__main__':
    gate = ResourceGate(16, False)
    print(gate.get_result_string())
    gate_with_perm = ResourceGate(16, True)
    print(gate_with_perm.get_result_string())
    adult_gate = ResourceGate(20, False)
    print(adult_gate.get_result_string())