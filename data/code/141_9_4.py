class LogicOperations:

    def __init__(self, value):
        self.value = value

    def and_(self, other):
        return LogicOperations(self.value and other.value)

    def or_(self, other):
        return LogicOperations(self.value or other.value)

    def not_(self):
        return LogicOperations(not self.value)
if __name__ == '__main__':
    a = LogicOperations(True)
    b = LogicOperations(False)
    print(a.and_(b).value)
    print(a.or_(b).value)
    print(b.not_().value)