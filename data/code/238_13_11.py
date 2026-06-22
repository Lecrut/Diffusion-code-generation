BOX_WIDTH = 6
BOX_HEIGHT = 4

def create_box(width=BOX_WIDTH, height=BOX_HEIGHT):
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2")
    top_bottom_row = ['#' * width]
    middle_rows = ['#' + ' ' * (width - 2) + '#'] * (height - 2)
    return top_bottom_row + middle_rows + top_bottom_row

if __name__ == '__main__':
    sample_box = create_box()
    for line in sample_box:
        print(line)