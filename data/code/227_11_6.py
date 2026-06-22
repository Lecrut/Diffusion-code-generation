def generate_star_pyramid(height):
    pyramid = []
    for i in range(height):
        row = ['*'] * (2 * i + 1)
        pyramid.append(' '.join(row))
    return pyramid

if __name__ == '__main__':
    sample_height = 4
    star_pyramid = generate_star_pyramid(sample_height)
    for line in star_pyramid:
        print(line)