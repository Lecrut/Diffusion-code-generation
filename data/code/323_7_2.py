class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def difference(self, other):
        diff_real = self.real - other.real
        diff_imag = self.imag - other.imag
        return ComplexNumber(diff_real, diff_imag)
if __name__ == '__main__':
    c1 = ComplexNumber(5 + 2j, 3 + 4j)
    c2 = ComplexNumber(1 + 7j, 6 + 8j)
    result = c1.difference(c2)
    print(f"Complex Number 1: {c1.real} + {c1.imag}j")
    print(f"Complex Number 2: {c2.real} + {c2.imag}j")
    print(f"Difference: {result.real} + {result.imag}j")