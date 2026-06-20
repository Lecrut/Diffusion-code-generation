class LazyBool:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if self.value() and not isinstance(other, LazyBool):
            return LazyBool(self.value() and bool(other))
        elif isinstance(other, LazyBool) and not other.value():
            return LazyBool(False)
        else:
            return other

    def __or__(self, other):
        if self.value() or not isinstance(other, LazyBool):
            return LazyBool(self.value() or bool(other))
        elif isinstance(other, LazyBool) and other.value():
            return LazyBool(True)
        else:
            return other

    def __not__(self):
        return LazyBool(not self.value())

    def value(self):
        if callable(self.value):
            return self.value()
        return self.value

if __name__ == '__main__':
    a = LazyBool(lambda: True)
    b = LazyBool(lambda: False)
    print((a & b).value())
    print((a | b).value())