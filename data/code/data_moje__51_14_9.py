def generate_number_pyramid(height=5):
    if height <= 0:
        return []
    pyramid = []
    for i in range(1, height + 1):
        numbers = [str(j) for j in range(1, i + 1)]
        line = ' '.join(numbers)
        pyramid.append(line)
    return pyramid

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    for line in result:
        print(line)