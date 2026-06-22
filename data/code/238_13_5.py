def create_box(width, height):
    return ['#' * width] + ['#' + ' ' * (width - 2) + '#'] * (height - 2) + ['#' * width]

if __name__ == '__main__':
    box = create_box(6, 4)
    for line in box:
        print(line)