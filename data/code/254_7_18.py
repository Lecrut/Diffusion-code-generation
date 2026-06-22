class ComplexNumberFinder:
    def __init__(self):
        self.complex_numbers = [
            3 + 4j,
            -1 - 1j,
            2 + 6j,
            -3 + 2j,
            0 - 2j
        ]

    def find_smallest_magnitude(self):
        if not self.complex_numbers:
            return None
        return min(self.complex_numbers, key=lambda x: abs(x))

if __name__ == '__main__':
    finder = ComplexNumberFinder()
    smallest = finder.find_smallest_magnitude()
    print(smallest)