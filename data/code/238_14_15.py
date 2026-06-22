class Box:
    def __init__(self, symbol='@', width=3, height=2):
        self.symbol = symbol
        self.width = width
        self.height = height

    def draw(self):
        return (self.symbol * self.width + '\n') * self.height

if __name__ == '__main__':
    box = Box()
    print(box.draw())