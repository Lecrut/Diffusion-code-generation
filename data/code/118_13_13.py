class ComplexMultiplier:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexMultiplier(real_part, imag_part)

if __name__ == '__main__':
    cm1 = ComplexMultiplier(3, 4)
    cm2 = ComplexMultiplier(1, -2)
    result = cm1.multiply(cm2)
    print(f"Result: {result.real} + {result.imag}j")