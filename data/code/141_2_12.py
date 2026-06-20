class LazyBool:
    TRUE = lambda: True
    FALSE = lambda: False

    @staticmethod
    def evaluate(func):
        return func() if callable(func) else func

    def __init__(self, value=True):
        self.value = value if isinstance(value, (bool, Lambda)) else self.TRUE

    def __and__(self, other):
        def and_func():
            return LazyBool.evaluate(self.value) and LazyBool.evaluate(other.value)
        return LazyBool(and_func)

    def __or__(self, other):
        def or_func():
            return LazyBool.evaluate(self.value) or LazyBool.evaluate(other.value)
        return LazyBool(or_func)

    def __not__(self):
        def not_func():
            return not LazyBool.evaluate(self.value)
        return LazyBool(not_func)

    def get_value(self):
        return self.value()

if __name__ == '__main__':
    a = LazyBool(True)
    b = LazyBool(False)
    print((a & b).get_value())
    print((a | b).get_value())
    print(~b.get_value())