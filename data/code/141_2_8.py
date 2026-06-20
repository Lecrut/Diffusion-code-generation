class LazyBool:
    def __init__(self, value):
        if callable(value):
            self.value = value
        else:
            self.value = lambda: value

    def and_(self, other):
        return LazyBool(lambda: self.value() and other.value())

    def or_(self, other):
        return LazyBool(lambda: self.value() or other.value())

    def not_(self):
        return LazyBool(lambda: not self.value())

    def evaluate(self):
        return self.value()

if __name__ == '__main__':
    a = LazyBool(True)
    b = LazyBool(False)
    print((a.and_(b)).evaluate())
    print((a.or_(b)).evaluate())
    print((~a).evaluate())