def generate_number_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        numbers = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        row = ' '.join(map(str, numbers))
        row = row.center(height * 2 - 1)
        pyramid.append(row)
    return pyramid
if __name__ == '__main__':
    height = 5
    pyramid = generate_number_pyramid(height)
    for row in pyramid:
        print(row)