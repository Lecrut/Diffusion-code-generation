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
    print(f"1. Logical AND (True and False): {logic.and_(True, False)}")
    print(f"2. Logical AND (True and True): {logic.and_(True, True)}")
    print(f"3. Logical OR (True or False): {logic.or_(True, False)}")
    print(f"4. Logical OR (False or False): {logic.or_(False, False)}")
    print(f"5. Logical NOT (not True): {logic.not_(True)}")
    print(f"6. Logical NOT (not False): {logic.not_(False)}")
    try:
        logic.and_(True, "not_a_bool")
    except TypeError as e:
        print(f"Error caught for type safety: {e}")
    try:
        logic.not_(10)
    except TypeError as e:
        print(f"Error caught for type safety: {e}")