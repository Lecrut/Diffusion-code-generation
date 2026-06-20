class LazyLogic:
    TRUE = True
    FALSE = False

    def __init__(self, value):
        self.value = value

    @staticmethod
    def lazy_eval(func):
        return lambda: func() if callable(func) else func

    def __and__(self, other):
        return LazyLogic(self.lazy_eval(lambda: self.value and other.value))

    def __or__(self, other):
        return LazyLogic(self.lazy_eval(lambda: self.value or other.value))

    def __not__(self):
        return LazyLogic(not self.value)

if __name__ == '__main__':
    a = LazyLogic(LazyLogic.TRUE)
    b = LazyLogic(LazyLogic.FALSE)
    print((a & b).value)
    print((a | b).value)