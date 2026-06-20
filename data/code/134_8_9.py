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
    manager.add_constraint("A")
    manager.add_constraint("B")
    print(f"Is 'A' mutually exclusive with existing constraints? {manager.is_mutually_exclusive('A')}")
    print(f"Is 'B' mutually exclusive with existing constraints? {manager.is_mutually_exclusive('B')}")
    print(f"Is 'C' mutually exclusive with existing constraints? {manager.is_mutually_exclusive('C')}")