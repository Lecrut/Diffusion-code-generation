def generate_star_square(size=3):
    return (''.join('* ' * size) for _ in range(size))

if __name__ == '__main__':
    for row in generate_star_square(3):
        print(row)