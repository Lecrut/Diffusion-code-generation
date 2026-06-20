class LogicalOperations:

    @staticmethod
    def and_(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Both inputs must be boolean values')
        return a and b

    @staticmethod
    def or_(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Both inputs must be boolean values')
        return a or b

    @staticmethod
    def not_(a):
        if not isinstance(a, bool):
            raise ValueError('Input must be a boolean value')
        return not a
if __name__ == '__main__':
    logical_ops = LogicalOperations()
    print(logical_ops.and_(True, False))
    print(logical_ops.or_(False, True))
    print(logical_ops.not_(True))