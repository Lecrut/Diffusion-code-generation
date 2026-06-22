class RectangleFiller:
    FILL_CHARACTER = 'X'

    @staticmethod
    def fill_block(width: int, height: int) -> str:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return '\n'.join([RectangleFiller.FILL_CHARACTER * width for _ in range(height)])

if __name__ == '__main__':
    print(RectangleFiller.fill_block(5, 3))