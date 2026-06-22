def generate_number_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        numbers = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        line = ''.join(str(num) for num in numbers)
        pyramid.append(line)
    return pyramid

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    for line in result:
        print(line)