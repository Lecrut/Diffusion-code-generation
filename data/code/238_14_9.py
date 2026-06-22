class TextBlock:
    def __init__(self, symbol):
        self.symbol = symbol

    def generate_box(self, width, height):
        return '\n'.join([self.symbol * width] * height)

if __name__ == '__main__':
    text_block = TextBlock('@')
    box = text_block.generate_box(3, 2)
    print(box)