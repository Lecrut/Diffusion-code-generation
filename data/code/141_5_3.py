class LogicalOperations:

    @staticmethod
    def AND(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError('Both inputs must be boolean')
        return a and b

    @staticmethod
    def OR(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError('Both inputs must be boolean')
        return a or b

    @staticmethod
    def NOT(a):
        if not isinstance(a, bool):
            raise TypeError('Input must be boolean')
        return not a
if __name__ == '__main__':
    logic = LogicalOperations()
    print(logic.AND(True, False))
    print(logic.OR(False, True))
    print(logic.NOT(True))