class RectangleFiller:
    WIDTH = 5
    HEIGHT = 5
    CHAR = '*'

    @staticmethod
    def fill_rectangle():
        return [[RectangleFiller.CHAR for _ in range(RectangleFiller.WIDTH)] for _ in range(RectangleFiller.HEIGHT)]

if __name__ == '__main__':
    filler = RectangleFiller()
    rectangle = filler.fill_rectangle()
    for row in rectangle:
        print(''.join(row))