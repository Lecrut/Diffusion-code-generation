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
    c = BooleanLogic(True)
    result_and = (a & b).value
    result_or = (b | c).value
    result_not = ~a.value
    print(result_and)
    print(result_or)
    print(result_not)