class LogicalOperations:
    def and_operation(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError('Both inputs must be boolean values')
        return a and b

    def or_operation(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError('Both inputs must be boolean values')
        return a or b

    def not_operation(self, a: bool) -> bool:
        if not isinstance(a, bool):
            raise TypeError('Input must be a boolean value')
        return not a

if __name__ == '__main__':
    logic = LogicalOperations()
    print(logic.and_operation(True, False))
    print(logic.or_operation(False, True))
    print(logic.not_operation(True))