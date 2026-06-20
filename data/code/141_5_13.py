def validate_input(value):
    if not isinstance(value, bool):
        raise TypeError('Inputs must be boolean values')

class LogicalOperations:
    def and_operation(self, a, b):
        validate_input(a)
        validate_input(b)
        return a and b
    
    def or_operation(self, a, b):
        validate_input(a)
        validate_input(b)
        return a or b
    
    def not_operation(self, a):
        validate_input(a)
        return not a

if __name__ == '__main__':
    logic = LogicalOperations()
    print(logic.and_operation(True, False))
    print(logic.or_operation(False, True))
    print(logic.not_operation(True))