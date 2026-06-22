def fill_rectangle(width, height):
    for _ in range(height):
        yield '*' * width

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    for row in fill_rectangle(sample_width, sample_height):
        print(row)