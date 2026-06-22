class RectangleFiller:
    def __init__(self, width=5, height=5, char='*'):
        self.width = width
        self.height = height
        self.char = char
        self.rectangle = self._create_rectangle()

    def _create_rectangle(self):
        return [[self.char for _ in range(self.width)] for _ in range(self.height)]

    def print_rectangle(self):
        for row in self.rectangle:
            print(''.join(row))

if __name__ == '__main__':
    filler = RectangleFiller()
    filler.print_rectangle()