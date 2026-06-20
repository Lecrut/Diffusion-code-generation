class SwapExample:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x

if __name__ == '__main__':
    example = SwapExample(5, 10)
    print(f"Before swap: x={example.x}, y={example.y}")
    example.swap()
    print(f"After swap: x={example.x}, y={example.y}")