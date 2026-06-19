class Number:

    def __init__(self, value):
        self.value = value

    def compare(self, other):
        if isinstance(other, Number):
            return self.value > other.value
        else:
            raise ValueError('Argument must be an instance of Number')
if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(5)
    result = num1.compare(num2)
    print(result)
    num3 = Number(7)
    num4 = Number(12)
    result = num3.compare(num4)
    print(result)