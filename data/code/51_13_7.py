def generate_symmetric_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = list(range(1, i + 1))
        full_sequence = numbers + numbers[-2::-1]
        line = ' '.join(map(str, full_sequence))
        result.append(spaces + line + spaces)
    return result

if __name__ == '__main__':
    pyramid = generate_symmetric_pyramid(8)
    for line in pyramid:
        print(line)