class LogicalOperators:
    TRUE = True
    FALSE = False

    @staticmethod
    def logical_and(a, b):
        return a and b

    @staticmethod
    def logical_or(a, b):
        return a or b

    @staticmethod
    def logical_not(a):
        return not a

if __name__ == '__main__':
    a = LogicalOperators.TRUE
    b = LogicalOperators.FALSE
    result_and = LogicalOperators.logical_and(a, b)
    result_or = LogicalOperators.logical_or(a, b)
    result_not = LogicalOperators.logical_not(a)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Logical AND ({a} and {b}): {result_and}")
    print(f"Logical OR ({a} or {b}): {result_or}")
    print(f"Logical NOT ({a}): {result_not}")