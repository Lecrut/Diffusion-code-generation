import matplotlib.pyplot as plt

class CheckerboardGenerator:
    SIZE = 8
    BLACK = 0
    WHITE = 1

    @staticmethod
    def generate_checkerboard():
        checkerboard = [[CheckerboardGenerator.BLACK if (i + j) % 2 == 0 else CheckerboardGenerator.WHITE for j in range(CheckerboardGenerator.SIZE)] for i in range(CheckerboardGenerator.SIZE)]
        return checkerboard

    @staticmethod
    def display_checkerboard(checkerboard):
        plt.imshow(checkerboard, cmap='gray')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    checkerboard = CheckerboardGenerator.generate_checkerboard()
    CheckerboardGenerator.display_checkerboard(checkerboard)