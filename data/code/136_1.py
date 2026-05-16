class LogicalOperators:
    def and_(self, a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError("Operands must be booleans")
        return a and b
    def or_(self, a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError("Operands must be booleans")
        return a or b
    def not_(self, a):
        if not isinstance(a, bool):
            raise TypeError("Operands must be a boolean")
        return not a
if __name__ == '__main__':
    logic = LogicalOperators()
    bool1 = True
    bool2 = False
    print(f"bool1: {bool1}, bool2: {bool2}")
    result_and = logic.and_(bool1, bool2)
    print(f"bool1 and bool2: {result_and}")
    result_or = logic.or_(bool1, bool2)
    print(f"bool1 or bool2: {result_or}")
    result_not = logic.not_(bool1)
    print(f"not bool1: {result_not}")
    try:
        logic.and_(bool1, "not_a_bool")
    except TypeError as e:
        print(f"Caught expected error: {e}")
    try:
        logic.not_(10)
    except TypeError as e:
        print(f"Caught expected error: {e}")