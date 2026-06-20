class LazyBoolean:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if not self.value:
            return self
        return other

    def __or__(self, other):
        if self.value:
            return self
        return other

    def __not__(self):
        return LazyBoolean(not self.value)

    def evaluate(self):
        return self.value
if __name__ == '__main__':
    a = LazyBoolean(True)
    b = LazyBoolean(False)
    print((a & b).evaluate())
    print((a | b).evaluate())
    print((~a).evaluate())