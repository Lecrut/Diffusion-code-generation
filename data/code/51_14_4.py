def generate_number_pyramid(height=5):
    pyramid = []
    for i in range(1, height + 1):
        row = ' '.join(str(i) for _ in range(i))
        pyramid.append(row.center(2 * height - 1))
    return pyramid

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    for line in result:
        print(line)