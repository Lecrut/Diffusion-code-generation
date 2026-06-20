class LazyBool:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return LazyBool(self.value() and other.value())

    def __or__(self, other):
        return LazyBool(self.value() or other.value())

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
    print((~a).value())