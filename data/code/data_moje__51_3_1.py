def generate_centered_pyramid(rows):
    return [''.join([str(i + 1) * j for j in [2 * (i + 1) - 1]]) for i in range(rows)]

if __name__ == '__main__':
    pyramid_lines = generate_centered_pyramid(7)
    for line in pyramid_lines:
        print(line)