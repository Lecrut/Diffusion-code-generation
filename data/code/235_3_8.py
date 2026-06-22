class InvertedPyramid:
    def print_pattern(self, width):
        for i in range(width, 0, -1):
            spaces = " " * (width - i)
            stars = "* " * i
            print(spaces + stars.strip())

if __name__ == '__main__':
    pyramid = InvertedPyramid()
    pyramid.print_pattern(9)