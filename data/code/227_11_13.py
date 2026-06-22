def generate_star_pyramid(height):
    stars = []
    for i in range(1, height + 1):
        row = '*' * (2 * i - 1)
        stars.append(row.center(height))
    return stars

if __name__ == '__main__':
    pyramid = generate_star_pyramid(4)
    for line in pyramid:
        print(line)