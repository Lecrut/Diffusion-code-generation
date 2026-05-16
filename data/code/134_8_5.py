class ConstraintManager:
    def __init__(self):
        self.constraints = set()
    def add_constraint(self, constraint):
        self.constraints.add(constraint)
    def is_mutually_exclusive(self, new_constraint):
        for existing_constraint in self.constraints:
            if existing_constraint == new_constraint:
                return True
        return False
if __name__ == '__main__':
    manager = ConstraintManager()
    constraint1 = "A == B"
    constraint2 = "A == C"
    constraint3 = "B == C"
    manager.add_constraint(constraint1)
    manager.add_constraint(constraint2)
    print(f"Checking if '{constraint1}' is mutually exclusive with existing constraints:")
    print(manager.is_mutually_exclusive(constraint1))
    print(f"Checking if '{constraint2}' is mutually exclusive with existing constraints:")
    print(manager.is_mutually_exclusive(constraint2))
    print(f"Checking if '{constraint3}' is mutually exclusive with existing constraints:")
    print(manager.is_mutually_exclusive(constraint3))
    manager.add_constraint(constraint3)
    print(f"Checking if '{constraint3}' is mutually exclusive with existing constraints:")
    print(manager.is_mutually_exclusive(constraint3))