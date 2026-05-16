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
    print(f"1. and_(True, True): {logic.and_(True, True)}")
    print(f"2. and_(True, False): {logic.and_(True, False)}")
    print(f"3. and_(False, True): {logic.and_(False, True)}")
    print(f"4. and_(False, False): {logic.and_(False, False)}")
    print(f"5. or_(True, True): {logic.or_(True, True)}")
    print(f"6. or_(True, False): {logic.or_(True, False)}")
    print(f"7. or_(False, True): {logic.or_(False, True)}")
    print(f"8. or_(False, False): {logic.or_(False, False)}")
    print(f"9. not_(True): {logic.not_(True)}")
    print(f"10. not_(False): {logic.not_(False)}")
    try:
        logic.and_(True, "hello")
    except TypeError as e:
        print(f"Error caught for type safety: {e}")
    try:
        logic.not_(123)
    except TypeError as e:
        print(f"Error caught for type safety: {e}")