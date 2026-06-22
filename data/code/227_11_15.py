def generate_star_pyramid(n):
    pyramid = []
    for i in range(n):
        row = [' ' * (n - i - 1) + '*' * (2 * i + 1)]
        pyramid.append(''.join(row))
    return pyramid

if __name__ == '__main__':
    star_pattern = generate_star_pyramid(4)
    for line in star_pattern:
        print(line)