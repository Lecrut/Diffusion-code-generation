class Number:

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be an integer or float')
        self.value = value

    def compare(self, other):
        if not isinstance(other, Number):
            raise ValueError('Argument must be an instance of Number')
        return self.value == other.value
if __name__ == '__main__':
    try:
        num1 = Number(5)
        num2 = Number(5.0)
        num3 = Number(10)
        print(num1.compare(num2))
        print(num1.compare(num3))
    except ValueError as e:
        print(e)