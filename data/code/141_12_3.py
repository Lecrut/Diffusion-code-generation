class BooleanLogic:

    def __init__(self, value):
        self.value = bool(value)

    def __and__(self, other):
        return BooleanLogic(self.value and other.value)

    def __or__(self, other):
        return BooleanLogic(self.value or other.value)

    def __not__(self):
        return BooleanLogic(not self.value)
if __name__ == '__main__':
    a = BooleanLogic(True)
    b = BooleanLogic(False)
    print((a & b).value)
    print((a | b).value)
    print(~b.value)