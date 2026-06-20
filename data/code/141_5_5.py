class LogicalOperations:

    def and_(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Inputs must be boolean')
        return a and b

    def or_(self, a: bool, b: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Inputs must be boolean')
        return a or b

    def not_(self, a: bool) -> bool:
        if not isinstance(a, bool):
            raise ValueError('Input must be boolean')
        return not a
if __name__ == '__main__':
    logic = LogicalOperations()
    print(logic.and_(True, False))
    print(logic.or_(False, True))
    print(logic.not_(True))