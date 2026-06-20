class ComplexNumberComparator:
    def __init__(self, complex1, complex2):
        self.complex1 = complex1
        self.complex2 = complex2

    def compare_by_abs(self):
        return abs(self.complex1), abs(self.complex2)

if __name__ == '__main__':
    comparator = ComplexNumberComparator(3 + 4j, 1 - 1j)
    abs1, abs2 = comparator.compare_by_abs()
    print(f"Absolute value of complex1: {abs1}")
    print(f"Absolute value of complex2: {abs2}")