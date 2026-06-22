def create_box(width=5, height=3):
    box = []
    for i in range(height):
        if i == 0 or i == height - 1:
            box.append('*' * width)
        else:
            box.append('*' + ' ' * (width - 2) + '*')
    return '\n'.join(box)

def print_box():
    width = 5
    height = 3
    box_pattern = create_box(width, height)
    print(box_pattern)

if __name__ == '__main__':
    sample_width = 7
    sample_height = 4
    custom_box = create_box(sample_width, sample_height)
    print(custom_box)