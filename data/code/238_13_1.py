def create_box(width, height):
    box = []
    for y in range(height):
        if y == 0 or y == height - 1:
            box.append('#' * width)
        else:
            box.append('#' + ' ' * (width - 2) + '#')
    return box

if __name__ == '__main__':
    sample_box = create_box(6, 4)
    for line in sample_box:
        print(line)