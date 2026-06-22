def create_box(width, height):
    top_bottom = ['#' * width]
    middle = ['#' + ' ' * (width - 2) + '#'] * (height - 2)
    return top_bottom + middle + top_bottom

if __name__ == '__main__':
    sample_width = 8
    sample_height = 5
    box = create_box(sample_width, sample_height)
    for line in box:
        print(line)