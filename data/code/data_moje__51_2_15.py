def generate_pyramid():
    rows = 6
    pyramid = []
    for i in range(1, rows + 1):
        line = ' '.join([str(i)] * i)
        pyramid.append(line)
    return pyramid

if __name__ == '__main__':
    result = generate_pyramid()
    for line in result:
        print(line)