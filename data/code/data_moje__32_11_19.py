class RectangleArea:
    WIDTH = 8
    HEIGHT = 6

    @staticmethod
    def compute(width, height):
        return width * height

if __name__ == '__main__':
    result = RectangleArea.compute(RectangleArea.WIDTH, RectangleArea.HEIGHT)
    print(result)