def create_box(width, height):
    return '@' * width + '\n' * (height - 1) + '@' * width

if __name__ == '__main__':
    box = create_box(3, 2)
    print(box)