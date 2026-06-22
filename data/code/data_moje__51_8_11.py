def generate_number_pyramid(rows):
    pyramid = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + str(i) * (2 * i - 1)
        pyramid.append(line)
    return '\n'.join(pyramid)

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    print(result)