class LazyLogic:

    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if not self.value:
            return False
        return other

    def __or__(self, other):
        if self.value:
            return True
        return other

    def __not__(self):
        return not self.value
if __name__ == '__main__':
    a = LazyLogic(True)
    b = LazyLogic(False)
    print(a & b)
    print(a | b)
    print(not a)