class BooleanLogic:

    def __init__(self, value):
        if not isinstance(value, bool):
            raise ValueError('Input must be a boolean value.')
        self.value = value

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
    result_or = (a | b).value
    result_not_b = ~b.value
    print(result_and)
    print(result_or)
    print(result_not_b)