def create_box(width=4, height=6):
    box = []
    for y in range(height):
        if y == 0 or y == height - 1:
            box.append('#' * width)
        else:
            box.append('#' + ' ' * (width - 2) + '#')
    return box

if __name__ == '__main__':
    print('\n'.join(create_box()))