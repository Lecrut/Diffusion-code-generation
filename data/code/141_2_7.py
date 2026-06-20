class LazyLogic:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if not self.value:
            return LazyLogic(False)
        return other

    def __or__(self, other):
        if self.value:
            return LazyLogic(True)
        return other

    def __not__(self):
        return LazyLogic(not self.value)
if __name__ == '__main__':
    a = LazyLogic(True)
    b = LazyLogic(False)
    print(a and b)
    print(a or b)
    print(not a)