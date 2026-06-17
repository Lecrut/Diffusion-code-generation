class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def difference(self, other):
        diff_real = self.real - other.real
        diff_imag = self.imag - other.imag
        return ComplexNumber(diff_real, diff_imag)
if __name__ == '__main__':
    c1 = ComplexNumber(5 + 2j, 1 + 3j)
    c2 = ComplexNumber(1 + 7j, 4 - 1j)
    result = c1.difference(c2)
    print(f"C1: {c1.real} + {c1.imag}j")
    print(f"C2: {c2.real} + {c2.imag}j")
    print(f"Difference (C1 - C2): {result.real} + {result.imag}j")