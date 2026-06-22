class RectangleFiller:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def fill_block(self) -> str:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return '\n'.join(['X' * self.width for _ in range(self.height)])

if __name__ == '__main__':
    filler = RectangleFiller(5, 3)
    print(filler.fill_block())