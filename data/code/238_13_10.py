class Box:
    def __init__(self, width=6, height=4):
        self.width = width
        self.height = height

    def create_box(self):
        box = []
        for y in range(self.height):
            if y == 0 or y == self.height - 1:
                box.append('#' * self.width)
            else:
                box.append('#' + ' ' * (self.width - 2) + '#')
        return box

if __name__ == '__main__':
    box_instance = Box(6, 4)
    sample_box = box_instance.create_box()
    for line in sample_box:
        print(line)