class NumberObject:

    def __init__(self, value):
        self.value = value

    def compare_to(self, other):
        if isinstance(other, NumberObject):
            return self.value - other.value
        else:
            raise ValueError('Argument must be an instance of NumberObject')
if __name__ == '__main__':
    num1 = NumberObject(10)
    num2 = NumberObject(5)
    print(num1.compare_to(num2))
    num3 = NumberObject(7)
    print(num2.compare_to(num3))
    num4 = NumberObject(10)
    print(num1.compare_to(num4))