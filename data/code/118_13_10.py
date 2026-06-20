class ComplexMultiplier:
    def multiply(self, a, b):
        real_part = a.real * b.real - a.imag * b.imag
        imag_part = a.real * b.imag + a.imag * b.real
        return complex(real_part, imag_part)

if __name__ == '__main__':
    multiplier = ComplexMultiplier()
    result = multiplier.multiply(3+4j, 1-2j)
    print(result)