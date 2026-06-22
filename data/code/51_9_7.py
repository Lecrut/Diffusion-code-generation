def build_symmetric_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        numbers = list(range(1, i + 1))
        numbers.extend(range(i - 1, 0, -1))
        line = ' '.join(map(str, numbers))
        padding = ' ' * (rows - i)
        result.append(padding + line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(build_symmetric_pyramid(6))