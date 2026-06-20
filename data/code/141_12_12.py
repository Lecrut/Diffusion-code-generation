class BooleanLogic:

    def __init__(self, value):
        self.value = bool(value)

    def __and__(self, other):
        return BooleanLogic(self.value and other.value)

    def __or__(self, other):
        return BooleanLogic(self.value or other.value)

    def __not__(self):
        return BooleanLogic(not self.value)

    def get_value(self):
        return self.value
if __name__ == '__main__':
    a = BooleanLogic(True)
    b = BooleanLogic(False)
    print(a.get_value())
    print(b.get_value())
    print((a & b).get_value())
    print((a | b).get_value())
    print((~a).get_value())
    print((~b).get_value())