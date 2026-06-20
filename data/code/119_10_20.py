class ValueSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap_values(self):
        self.x, self.y = self.y, self.x

    def get_values(self):
        return self.x, self.y

if __name__ == '__main__':
    swapper = ValueSwapper(5, 10)
    swapper.swap_values()
    print(f"Swapped values: x={swapper.get_values()[0]}, y={swapper.get_values()[1]}")