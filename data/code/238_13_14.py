class BoxCreator:
    TOP_BOTTOM_EDGE = '#'
    INNER_EDGE = '#'

    @staticmethod
    def create_box(width, height):
        if width < 2 or height < 2:
            raise ValueError("Width and height must be at least 2")
        
        box = [BoxCreator.TOP_BOTTOM_EDGE * width]
        for _ in range(height - 2):
            box.append(BoxCreator.INNER_EDGE + ' ' * (width - 2) + BoxCreator.INNER_EDGE)
        box.append(BoxCreator.TOP_BOTTOM_EDGE * width)
        return box

if __name__ == '__main__':
    sample_box = BoxCreator.create_box(6, 4)
    for line in sample_box:
        print(line)