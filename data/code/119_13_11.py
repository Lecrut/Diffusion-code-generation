class NumberSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x
        return self.x, self.y

if __name__ == '__main__':
    swapper = NumberSwapper(100, 200)
    print(f"Before swap: x={swapper.x}, y={swapper.y}")
    swapper.swap()
    print(f"After swap: x={swapper.x}, y={swapper.y}")