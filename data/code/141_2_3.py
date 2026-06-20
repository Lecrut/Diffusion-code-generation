class LazyLogic:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return LazyLogic(self.value and other.value)

    def __or__(self, other):
        return LazyLogic(self.value or other.value)

    def __not__(self):
        return LazyLogic(not self.value)

    def evaluate(self):
        return self.value
if __name__ == '__main__':
    a = LazyLogic(True)
    b = LazyLogic(False)
    c = LazyLogic(True)
    print((a & b).evaluate())
    print((a | b).evaluate())
    print(~b.evaluate())