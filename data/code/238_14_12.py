class Box:
    def __init__(self, symbol='@'):
        self.symbol = symbol

    def draw(self):
        return f"{self.symbol * 3}\n{self.symbol * 3}\n"

if __name__ == '__main__':
    box = Box()
    print(box.draw())