class NumericSwapper:
    def __init__(self, a, b):
        self.values = [a, b]

    def swap(self):
        self.values[0], self.values[1] = self.values[1], self.values[0]

if __name__ == '__main__':
    swapper = NumericSwapper(5, 10)
    print("Original values:", swapper.values)
    swapper.swap()
    print("Swapped values:", swapper.values)