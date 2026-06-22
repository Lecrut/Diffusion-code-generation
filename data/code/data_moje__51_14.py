def generate_number_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        line = ' '.join(str(i) for _ in range(i))
        pyramid.append(line)
    return pyramid

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    print(result)