class CheckerboardGenerator:
    CHAR_1 = '.'
    CHAR_2 = '#'

    @staticmethod
    def generate(width, height):
        checkerboard = []
        for y in range(height):
            row = ''.join([CheckerboardGenerator.CHAR_1 if (x + y) % 2 == 0 else CheckerboardGenerator.CHAR_2 for x in range(width)])
            checkerboard.append(row)
        return checkerboard

if __name__ == '__main__':
    width, height = 8, 6
    board = CheckerboardGenerator.generate(width, height)
    for row in board:
        print(row)