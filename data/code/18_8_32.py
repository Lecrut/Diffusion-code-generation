class Number:

    def __init__(self, value):
        self.value = value

    def compare(self, other):
        if isinstance(other, Number):
            return self.value - other.value
        else:
            raise ValueError('Argument must be an instance of Number')
if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(5)
    result = num1.compare(num2)
    print(result)
    num3 = Number(7)
    result2 = num3.compare(Number(7))
    print(result2)
    num4 = Number(3)
    result3 = num4.compare(Number(8))
    print(result3)