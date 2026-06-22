def create_box(width=4, height=6):
    return ['#' * width] + ['#' + ' ' * (width - 2) + '#'] * (height - 2) + ['#' * width]

if __name__ == '__main__':
    box = create_box()
    for line in box:
        print(line)