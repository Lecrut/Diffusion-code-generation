import sys
class ValueMatcher:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if isinstance(other, ValueMatcher):
            return self.value == other.value
        elif other is None or not hasattr(other, '__bool__'):
            try:
                bool(self.value) and bool(other)
                return True
            except TypeError:
                pass
            return False
        else:
            return NotImplemented
    def __repr__(self):
        return f"ValueMatcher({self.value!r})"
if __name__ == '__main__':
    matcher1 = ValueMatcher(42)
    matcher2 = ValueMatcher("hello")
    none_matcher = None
    print(f"{matcher1} equals {matcher2}: {matcher1 == matcher2}")
    print(f"{matcher1} equals {none_matcher}: {matcher1 == none_matcher}")
    print(repr(matcher1))