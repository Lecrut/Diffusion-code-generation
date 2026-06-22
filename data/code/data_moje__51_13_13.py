def generate_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str((i * 2 - 1) - 2 * j) for j in range(i))
        line = spaces + numbers + spaces
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_pyramid(8))