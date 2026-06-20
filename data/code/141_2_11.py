class LazyBool:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if not self.value:
            return LazyBool(False)
        return other

    def __or__(self, other):
        if self.value:
            return LazyBool(True)
        return other

    def __not__(self):
        return LazyBool(not self.value)

    def evaluate(self):
        if callable(self.value):
            self.value = self.value()
        return self.value
if __name__ == '__main__':
    a = LazyBool(lambda: False)
    b = LazyBool(True)
    c = LazyBool(False)
    print(a & b)
    print((a & b).evaluate())
    print(b | c)
    print((b | c).evaluate())
    print(not a)
    print((not a).evaluate())