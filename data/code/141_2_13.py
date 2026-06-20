class LazyBool:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if not self.value:
            return LazyBool(False)
        return LazyBool(other)

    def __or__(self, other):
        if self.value:
            return LazyBool(True)
        return LazyBool(other)

    def __not__(self):
        return LazyBool(not self.value)

    def evaluate(self):
        return self.value
if __name__ == '__main__':
    a = LazyBool(True)
    b = LazyBool(False)
    print((a & b).evaluate())
    print((a | b).evaluate())
    print((~a).evaluate())