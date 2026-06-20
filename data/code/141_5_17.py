class LogicalOperations:
    @staticmethod
    def validate_input(value):
        if not isinstance(value, bool):
            raise TypeError('Input must be a boolean value')

    @staticmethod
    def AND(a, b):
        LogicalOperations.validate_input(a)
        LogicalOperations.validate_input(b)
        return a and b

    @staticmethod
    def OR(a, b):
        LogicalOperations.validate_input(a)
        LogicalOperations.validate_input(b)
        return a or b

    @staticmethod
    def NOT(a):
        LogicalOperations.validate_input(a)
        return not a

if __name__ == '__main__':
    logic = LogicalOperations()
    print(logic.AND(True, False))
    print(logic.OR(False, True))
    print(logic.NOT(True))