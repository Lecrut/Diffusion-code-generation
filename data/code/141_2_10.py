class LazyBool:
    def __init__(self, value):
        if not callable(value) and not isinstance(value, bool):
            raise ValueError("Value must be a boolean or a callable returning a boolean")
        self.value = value

    def __and__(self, other):
        return LazyBool(lambda: self.value() and other.value())

    def __or__(self, other):
        return LazyBool(lambda: self.value() or other.value())

    def __not__(self):
        return LazyBool(lambda: not self.value())

    def evaluate(self):
        if callable(self.value):
            return self.value()
        return self.value

if __name__ == '__main__':
    a = LazyBool(True)
    b = LazyBool(False)
    print((a & b).evaluate())
    print((a | b).evaluate())