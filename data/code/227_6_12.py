class StarPyramid:
    def __init__(self, height):
        self.height = height

    def print_pattern(self):
        for i in range(1, self.height + 1):
            print(" " * (self.height - i) + "* " * (2 * i - 1))

if __name__ == '__main__':
    pyramid = StarPyramid(3)
    pyramid.print_pattern()