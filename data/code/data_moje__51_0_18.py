def generate_right_aligned_pyramid(rows):
    pyramid = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + str(i) * i
        pyramid.append(line)
    return pyramid
if __name__ == '__main__':
    result = generate_right_aligned_pyramid(5)
    for line in result:
        print(line)