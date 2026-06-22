class BooleanOp:
    def __init__(self, initial_value):
        self._value = initial_value

    def get_value(self):
        return self._value

    def negate(self):
        self._value = not self._value
        return self._value

if __name__ == '__main__':
    op1 = BooleanOp(True)
    op2 = BooleanOp(False)
    print(op1.negate())
    print(op2.negate())