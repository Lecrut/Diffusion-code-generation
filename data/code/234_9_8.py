import cv2

class CheckerboardDrawer:
    def __init__(self, cell_size, rows, cols):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.image = None

    def draw_checkerboard(self):
        self.image = np.zeros((self.rows * self.cell_size, self.cols * self.cell_size, 3), dtype=np.uint8)
        for i in range(self.rows):
            for j in range(self.cols):
                if (i + j) % 2 == 0:
                    cv2.rectangle(self.image, (j * self.cell_size, i * self.cell_size), ((j + 1) * self.cell_size, (i + 1) * self.cell_size), (255, 255, 255), -1)
                else:
                    cv2.rectangle(self.image, (j * self.cell_size, i * self.cell_size), ((j + 1) * self.cell_size, (i + 1) * self.cell_size), (0, 0, 0), -1)

if __name__ == '__main__':
    drawer = CheckerboardDrawer(cell_size=50, rows=8, cols=8)
    drawer.draw_checkerboard()
    cv2.imshow('Checkerboard', drawer.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()