class BoolLogic:

    def __init__(self, value):
        self.value = bool(value)

    def __and__(self, other):
        return BoolLogic(self.value and other.value)

    def __or__(self, other):
        return BoolLogic(self.value or other.value)

    def __not__(self):
        return BoolLogic(not self.value)

    def get_value(self):
        return self.value
if __name__ == '__main__':
    a = BoolLogic(True)
    b = BoolLogic(False)
    print(a & b)
    print(a | b)
    print(~a)
    print(~b)