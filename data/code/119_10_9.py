class ValueSwapper:
    def __init__(self, x=5, y=10):
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x

    def get_values(self):
        return self.x, self.y

if __name__ == '__main__':
    swapper = ValueSwapper()
    print(f"Original values: x={swapper.get_values()[0]}, y={swapper.get_values()[1]}")
    swapper.swap()
    print(f"Swapped values: x={swapper.get_values()[0]}, y={swapper.get_values()[1]}")