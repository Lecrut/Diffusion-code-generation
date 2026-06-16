import sys
class ValueMatcher:
    def __init__(self, target_value):
        self.target = target_value
    def __eq__(self, other):
        if self.target is None and other is None:
            return True
        try:
            result = (self.target == other)
        except TypeError:
            return False
        return result
if __name__ == '__main__':
    matcher1 = ValueMatcher(42)
    matcher2 = ValueMatcher("hello")
    test_cases = [
        (ValueMatcher(42), 42, True),
        (ValueMatcher(None), None, True),
        (ValueMatcher(42), "42", False),
        (ValueMatcher(10), 5, False),
        (None, ValueMatcher(None), True),                                                                         
    ]
    for item, expected_value, expected_result in test_cases:
        is_match = item == expected_value or (isinstance(item, ValueMatcher) and item.target == expected_value)
        print(f"Comparing {item} with {expected_value}: Expected={expected_result}, Got={is_match}")
    assert matcher1.__eq__(42) is True
    assert matcher1.__eq__("wrong") is False
    assert ValueMatcher(None).__eq__(None) is True
    print("All assertions passed.")