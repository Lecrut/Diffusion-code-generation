import sys
class ValueMatcher:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        try:
            lhs = self.value
            rhs = other.value
            if lhs is None and rhs is None:
                return True
            elif lhs is None or rhs is None:
                return False
            else:
                return str(lhs) == str(rhs)
        except Exception:
            return NotImplemented
if __name__ == '__main__':
    matcher1 = ValueMatcher("test")
    matcher2 = ValueMatcher("test")
    matcher3 = ValueMatcher(None)
    assert matcher1.__eq__(matcher2), "Equal strings should match"
    assert not matcher1.__eq__(ValueMatcher("other")), "Different strings should not match"
    assert matcher3.__eq__(ValueMatcher(None)), "None values should match"
    print("All assertions passed.")