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
    a = True
    b = False
    print(f"a: {a}, b: {b}")
    result_and = logic.and_(a, b)
    print(f"a and b: {result_and}")
    result_or = logic.or_(a, b)
    print(f"a or b: {result_or}")
    result_not = logic.not_(a)
    print(f"not a: {result_not}")
    try:
        logic.and_(a, "not_a")
    except TypeError as e:
        print(f"Caught expected error for type safety: {e}")
    try:
        logic.not_(10)
    except TypeError as e:
        print(f"Caught expected error for type safety: {e}")