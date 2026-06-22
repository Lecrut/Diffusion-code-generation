class RectangleFiller:
    DEFAULT_SYMBOL = "*"

    @staticmethod
    def fill_rectangle(width, height, symbol=DEFAULT_SYMBOL):
        return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    filler = RectangleFiller()
    width = 10
    height = 5
    result = filler.fill_rectangle(width, height)
    print("\n".join(result))