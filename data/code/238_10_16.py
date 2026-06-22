class BoxGenerator:
    def __init__(self, width=5, height=3):
        self.width = width
        self.height = height

    def generate_box(self):
        box = []
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                row = '*' * self.width
            else:
                row = '*' + ' ' * (self.width - 2) + '*'
            box.append(row)
        return '\n'.join(box)

if __name__ == '__main__':
    generator = BoxGenerator(5, 3)
    print(generator.generate_box())