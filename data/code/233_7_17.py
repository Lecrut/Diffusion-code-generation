def fill_rectangle(width, height):
    return (('*' * width) for _ in range(height))

if __name__ == '__main__':
    sample_width = 8
    sample_height = 5
    rectangle = list(fill_rectangle(sample_width, sample_height))
    print('\n'.join(rectangle))