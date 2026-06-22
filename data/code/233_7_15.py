class RectangleFiller:
    SYMBOL = '*'

    @staticmethod
    def fill_rectangle(width, height):
        return (RectangleFiller.SYMBOL * width for _ in range(height))

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    filled_rectangle = list(RectangleFiller.fill_rectangle(sample_width, sample_height))
    print(filled_rectangle)