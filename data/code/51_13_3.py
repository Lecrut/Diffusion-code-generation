def generate_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(min(j, 2 * i - 1 - j + 1)) for j in range(1, 2 * i))
        line = spaces + numbers
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_pyramid(8))