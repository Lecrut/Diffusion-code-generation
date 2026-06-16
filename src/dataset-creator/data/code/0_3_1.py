class ValueChecker:
    def check_equality(self, value1, value2, custom_logic=None):
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return abs(value1 - value2) < 0.0001
        try:
            result = False
            if callable(custom_logic):
                result = custom_logic(value1, value2)
            else:
                result = value1 == value2
            return bool(result)
        except Exception as e:
            raise TypeError(f"Comparison failed due to {type(e).__name__}: {e}")
if __name__ == '__main__':
    checker = ValueChecker()
    assert checker.check_equality(5, 5) is True
    assert checker.check_equality(0.3 + 0.6, 0.9) is True
    assert checker.check_equality("hello", "world") is False
    def my_custom_compare(a, b):
        return isinstance(a, str) and len(b) == 0
    assert checker.check_equality("test", "", custom_logic=my_custom_compare) is True
    try:
        result = checker.check_equality(None, "None")
        print(f"Result for None vs 'None': {result}")
    except TypeError as e:
        pass
    print("All tests completed.")