class CheckerboardGenerator:
    CHARACTERS = ('.', '#')

    @staticmethod
    def generate(width, height):
        checkerboard = []
        for y in range(height):
            row = ''.join(CheckerboardGenerator.CHARACTERS[(x + y) % 2] for x in range(width))
            checkerboard.append(row)
        return checkerboard

if __name__ == '__main__':
    generator = CheckerboardGenerator()
    board = generator.generate(8, 6)
    for row in board:
        print(row)