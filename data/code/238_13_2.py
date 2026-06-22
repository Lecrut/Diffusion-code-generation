def create_box(width, height):
    box = []
    for i in range(height):
        if i == 0 or i == height - 1:
            box.append('#' * width)
        else:
            box.append('#' + ' ' * (width - 2) + '#')
    return box

if __name__ == '__main__':
    sample_box = create_box(6, 4)
    for line in sample_box:
        print(line)