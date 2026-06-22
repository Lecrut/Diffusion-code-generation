class Number:

    def __init__(self, value):
        self.value = value

    @staticmethod
    def _is_valid_number(other):
        return isinstance(other, Number)

    def compare(self, other):
        if not self._is_valid_number(other):
            raise ValueError('Argument must be an instance of Number')
        return self.value == other.value
if __name__ == '__main__':
    num1 = Number(5)
    num2 = Number(5)
    num3 = Number(10)
    print(num1.compare(num2))
    print(num1.compare(num3))