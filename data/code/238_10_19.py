class Box:
    def __init__(self, width=5, height=3):
        self.width = width
        self.height = height

    def print_box(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print('*' * self.width)
            else:
                print('*' + ' ' * (self.width - 2) + '*')

if __name__ == '__main__':
    box = Box(5, 3)
    box.print_box()