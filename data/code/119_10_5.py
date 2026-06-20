class ValueSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x
        return self.x, self.y

if __name__ == '__main__':
    swapper = ValueSwapper(5, 10)
    print(f"Original values: x={swapper.x}, y={swapper.y}")
    swapper.swap()
    print(f"Swapped values: x={swapper.x}, y={swapper.y}")