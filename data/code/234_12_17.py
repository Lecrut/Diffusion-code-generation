from PIL import Image

class Checkerboard:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, size):
        self.size = size

    @staticmethod
    def create_square(color, size):
        return Image.new('RGB', (size, size), color=color)

    def get_board(self):
        board = Image.new('RGB', (self.size * 20, self.size * 20))
        for i in range(self.size):
            for j in range(self.size):
                square_size = 20
                if (i + j) % 2 == 0:
                    color = Checkerboard.BLACK
                else:
                    color = Checkerboard.WHITE
                board.paste(Checkerboard.create_square(color, square_size), (j * square_size, i * square_size))
        return board

if __name__ == '__main__':
    board_size = 8
    cb = Checkerboard(board_size)
    image = cb.get_board()
    image.show()