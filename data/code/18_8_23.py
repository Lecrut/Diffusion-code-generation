class Number:

    def __init__(self, value):
        self.value = value

    def compare(self, other):
        if not isinstance(other, Number):
            raise ValueError('Argument must be an instance of Number')
        return self.value == other.value
if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(10)
    num3 = Number(20)
    print(num1.compare(num2))
    print(num1.compare(num3))