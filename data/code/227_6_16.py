class StarPyramidBuilder:
    @staticmethod
    def build_pyramid(height):
        if height <= 0:
            return []
        pyramid = []
        for i in range(1, height + 1):
            row = " " * (height - i) + "* " * (2 * i - 1)
            pyramid.append(row)
        return pyramid

    @staticmethod
    def print_pyramid(pyramid):
        for row in pyramid:
            print(row)

if __name__ == '__main__':
    pyramid = StarPyramidBuilder.build_pyramid(3)
    StarPyramidBuilder.print_pyramid(pyramid)