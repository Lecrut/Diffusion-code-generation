class InvertedPyramid:
    def __init__(self, base_width):
        self.base_width = base_width

    def print_pyramid(self):
        for i in range(self.base_width // 2, -1, -1):
            spaces = ' ' * (i + 1)
            stars = '*' * (self.base_width - 2 * i - 1)
            print(spaces + stars)

if __name__ == '__main__':
    pyramid = InvertedPyramid(9)
    pyramid.print_pyramid()