class ValueSwapper:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def swap(self):
        self.value1, self.value2 = self.value2, self.value1

if __name__ == '__main__':
    swapper = ValueSwapper(5, 10)
    print(f"Original values: x={swapper.value1}, y={swapper.value2}")
    swapper.swap()
    print(f"Swapped values: x={swapper.value1}, y={swapper.value2}")