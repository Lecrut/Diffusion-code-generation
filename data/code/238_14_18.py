class TextBox:
    def __init__(self):
        self.symbol = '@'

    def create_box(self, rows, cols):
        return '\n'.join([self.symbol * cols for _ in range(rows)])

if __name__ == '__main__':
    box = TextBox()
    result = box.create_box(3, 2)
    print(result)