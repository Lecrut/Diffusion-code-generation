def generate_star_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        row = ['*'] * (2 * i - 1)
        center = len(row) // 2
        row[center] = '*'
        for j in range(center - 1, -1, -1):
            if j != center:
                row[j] = ' '
                row[2 * center - j - 1] = ' '
        pyramid.append(''.join(row))
    return pyramid

if __name__ == '__main__':
    star_pyramid = generate_star_pyramid(4)
    for line in star_pyramid:
        print(line)