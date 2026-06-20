class NumberSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x

if __name__ == '__main__':
    swapper = NumberSwapper(10, 20)
    print(f"Before swap: x={swapper.x}, y={swapper.y}")
    swapper.swap()
    print(f"After swap: x={swapper.x}, y={swapper.y}")