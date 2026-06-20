class LogicalOperation:

    def __init__(self, value):
        self.value = value

    def and_(self, other):
        return LogicalOperation(self.value and other.value)

    def or_(self, other):
        return LogicalOperation(self.value or other.value)

    def not_(self):
        return LogicalOperation(not self.value)

    def get_value(self):
        return self.value
if __name__ == '__main__':
    op1 = LogicalOperation(True)
    op2 = LogicalOperation(False)
    result_and = op1.and_(op2).get_value()
    result_or = op1.or_(op2).get_value()
    result_not = op1.not_().get_value()
    print(result_and)
    print(result_or)
    print(result_not)