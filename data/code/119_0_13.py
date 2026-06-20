class Swapper:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swap(self):
        self.a, self.b = self.b, self.a

if __name__ == '__main__':
    swapper = Swapper(5, 10)
    swapper.swap()
    print(f"x: {swapper.a}, y: {swapper.b}")