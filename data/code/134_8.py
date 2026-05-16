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
    constraint1 = "A"
    constraint2 = "B"
    constraint3 = "A"
    manager.add_constraint(constraint1)
    manager.add_constraint(constraint2)
    print(f"Is '{constraint1}' mutually exclusive with existing constraints? {manager.is_mutually_exclusive(constraint1)}")
    print(f"Is '{constraint2}' mutually exclusive with existing constraints? {manager.is_mutually_exclusive(constraint2)}")
    print(f"Is '{constraint3}' mutually exclusive with existing constraints? {manager.is_mutually_exclusive(constraint3)}")
    manager.add_constraint("C")
    print(f"Is 'C' mutually exclusive with existing constraints? {manager.is_mutually_exclusive('C')}")