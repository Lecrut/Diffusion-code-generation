class NumberSwapper:
    def __init__(self, value1, value2):
        self.values = [value1, value2]

    def swap(self):
        self.values[0], self.values[1] = self.values[1], self.values[0]
        return self.values

if __name__ == '__main__':
    swapper = NumberSwapper(5, 10)
    print(f"Original values: {swapper.values}")
    swapped_values = swapper.swap()
    print(f"Swapped values: {swapped_values}")