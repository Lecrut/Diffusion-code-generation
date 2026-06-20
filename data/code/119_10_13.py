class ValueSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x

if __name__ == '__main__':
    swapper = ValueSwapper(5, 10)
    swapper.swap()
    print(f"x: {swapper.x}, y: {swapper.y}")