class RectangleFiller:
    DEFAULT_SIZE = 8

    @staticmethod
    def validate_size(size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")

    @classmethod
    def fill_rectangle(cls, size=DEFAULT_SIZE):
        cls.validate_size(size)
        return [['#' for _ in range(size)] for _ in range(size)]

if __name__ == '__main__':
    filler = RectangleFiller()
    grid = filler.fill_rectangle(5)
    print(grid)