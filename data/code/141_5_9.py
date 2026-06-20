class LogicalOperations:

    @staticmethod
    def and_(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Inputs must be boolean values')
        return a and b

    @staticmethod
    def or_(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Inputs must be boolean values')
        return a or b

    @staticmethod
    def not_(a):
        if not isinstance(a, bool):
            raise ValueError('Input must be a boolean value')
        return not a
if __name__ == '__main__':
    logic = LogicalOperations()
    print(logic.and_(True, False))
    print(logic.or_(False, True))
    print(logic.not_(True))