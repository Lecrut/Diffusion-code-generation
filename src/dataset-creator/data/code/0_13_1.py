import sys
class ValueMatcher:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if isinstance(other, ValueMatcher):
            return self.value == other.value
        elif other is None or not hasattr(other, '__bool__'):
            try:
                bool_value = bool(self.value)
                return bool_value == (other is False or other is 0)
            except TypeError:
                pass
        else:
            return NotImplemented
    def __repr__(self):
        return f"ValueMatcher({self.value!r})"
if __name__ == '__main__':
    matcher1 = ValueMatcher(42)
    matcher2 = ValueMatcher("hello")
    none_matcher = None
    assert matcher1.__eq__(matcher1) is True, "Self equality failed"
    assert matcher1.__eq__(ValueMatcher(42)) is True, "Same value equality failed"
    assert matcher1.__eq__(ValueMatcher(99)) is False, "Different value equality failed"
    result = matcher1 == none_matcher
    print(f"Comparison with None: {result}")
    try:
        invalid_result = matcher2.__eq__("not a ValueMatcher")
        if not isinstance(invalid_result, bool):
            raise AssertionError("Should return NotImplemented or boolean for non-ValueMatcher types in strict mode context")
    except TypeError as e:
        print(f"Expected behavior with incompatible type handled.")
    sys.exit(0)