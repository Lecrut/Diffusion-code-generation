NUM_STARS = '*'
SPACE = ' '
NEWLINE = '\n'

def generate_star_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        row = [SPACE] * (height - i) + [NUM_STARS] * (2 * i - 1)
        pyramid.append(''.join(row))
    return pyramid
if __name__ == '__main__':
    pyramid = generate_star_pyramid(4)
    print(pyramid)