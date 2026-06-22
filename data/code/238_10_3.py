def generate_box(width=5, height=3):
    box = []
    for i in range(height):
        if i == 0 or i == height - 1:
            row = '*' * width
        else:
            row = '*' + ' ' * (width - 2) + '*'
        box.append(row)
    return '\n'.join(box)

if __name__ == '__main__':
    sample_width = 7
    sample_height = 4
    print(generate_box(sample_width, sample_height))