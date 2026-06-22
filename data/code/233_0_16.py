class RectangleFiller:
    CHAR = '*'

    @staticmethod
    def fill_rectangle():
        return [[RectangleFiller.CHAR for _ in range(5)] for _ in range(5)]

if __name__ == '__main__':
    filler = RectangleFiller()
    rectangle = filler.fill_rectangle()
    for row in rectangle:
        print(''.join(row))