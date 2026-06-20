class LazyBool:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        if callable(self.value):
            return self.value()
        return self.value

    def __and__(self, other):
        def and_result():
            result = self.evaluate() and other.evaluate()
            return LazyBool(result)
        return and_result

    def __or__(self, other):
        def or_result():
            result = self.evaluate() or other.evaluate()
            return LazyBool(result)
        return or_result

    def __not__(self):
        def not_result():
            result = not self.evaluate()
            return LazyBool(result)
        return not_result

if __name__ == '__main__':
    a = LazyBool(lambda: True)
    b = LazyBool(lambda: False)
    print((a & b).evaluate())
    print((a | b).evaluate())