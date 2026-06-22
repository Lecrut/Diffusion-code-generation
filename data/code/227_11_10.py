def generate_star_pyramid(n):
    pyramid = []
    for i in range(n):
        row = [' ' * (n - i - 1)] + ['*'] * (2 * i + 1) + [' ' * (n - i - 1)]
        pyramid.append(''.join(row))
    return pyramid

if __name__ == '__main__':
    height = 4
    star_pyramid = generate_star_pyramid(height)
    for row in star_pyramid:
        print(row)