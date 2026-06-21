class BooleanChecker:
    TRUE_STATE = True
    FALSE_STATE = False

    @staticmethod
    def is_any_true(value, values):
        if not isinstance(value, bool):
            raise ValueError("First argument must be a boolean")
        if not isinstance(values, list):
            raise ValueError("Second argument must be a list")
        for item in values:
            if not isinstance(item, bool):
                raise ValueError("All items in the list must be booleans")
        
        if value is BooleanChecker.TRUE_STATE:
            return BooleanChecker.TRUE_STATE
        
        for val in values:
            if val is BooleanChecker.TRUE_STATE:
                return BooleanChecker.TRUE_STATE
        
        return BooleanChecker.FALSE_STATE

if __name__ == '__main__':
    result1 = BooleanChecker.is_any_true(False, [False, False, False])
    print(result1)
    result2 = BooleanChecker.is_any_true(True, [False, False, False])
    print(result2)
    result3 = BooleanChecker.is_any_true(False, [False, True, False])
    print(result3)