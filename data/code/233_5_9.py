class RectangleFiller:
    BLOCK_CHARACTER = 'X'

    @staticmethod
    def fill_block(width: int, height: int) -> str:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        
        rectangle = []
        for _ in range(height):
            row = [RectangleFiller.BLOCK_CHARACTER] * width
            rectangle.append(''.join(row))
        return '\n'.join(rectangle)

if __name__ == '__main__':
    filler = RectangleFiller()
    print(filler.fill_block(5, 3))