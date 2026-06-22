class FractionComparator:
    def __init__(self, ratio1, ratio2):
        self.ratio1 = ratio1
        self.ratio2 = ratio2

    def are_equivalent(self):
        return self.ratio1 * self.ratio2 == 1

if __name__ == '__main__':
    comparator = FractionComparator(3, 9)
    result = comparator.are_equivalent()
    print(f"Fractions are equivalent: {result}")