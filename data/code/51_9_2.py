def build_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        numbers = list(range(1, i)) + [i] + list(range(i - 1, 0, -1))
        line_str = ' '.join(map(str, numbers))
        padding = (rows - i) * 2
        result.append(' ' * padding + line_str)
    return '\n'.join(result)

if __name__ == '__main__':
    print(build_pyramid(6))