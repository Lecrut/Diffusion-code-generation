class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @classmethod
    def is_identical(cls, instance1, instance2):
        return instance1.__dict__ == instance2.__dict__
if __name__ == '__main__':
    num1 = ComplexNumber(3, 4)
    num2 = ComplexNumber(3, 4)
    num3 = ComplexNumber(5, 6)
    print(ComplexNumber.is_identical(num1, num2))
    print(ComplexNumber.is_identical(num1, num3))