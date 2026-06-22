import cv2

class CheckerboardDrawer:
    def __init__(self, width=800, height=600, cell_size=50):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.image = None

    def create_checkerboard(self):
        self.image = np.zeros((self.height, self.width), dtype=np.uint8)
        for i in range(0, self.height, self.cell_size):
            for j in range(0, self.width, self.cell_size):
                if (i // self.cell_size + j // self.cell_size) % 2 == 0:
                    cv2.rectangle(self.image, (j, i), (j + self.cell_size, i + self.cell_size), 255, -1)

    def save_image(self, filename="checkerboard.png"):
        if self.image is not None:
            cv2.imwrite(filename, self.image)

if __name__ == '__main__':
    checkerboard_drawer = CheckerboardDrawer(width=800, height=600, cell_size=50)
    checkerboard_drawer.create_checkerboard()
    checkerboard_drawer.save_image("checkerboard.png")