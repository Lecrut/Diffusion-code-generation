def generate_rectangle(width, height):
    return [width * '#' for _ in range(height)]

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    print(generate_rectangle(sample_width, sample_height))