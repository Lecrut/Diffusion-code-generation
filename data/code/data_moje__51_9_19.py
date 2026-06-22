def build_symmetric_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        numbers = list(range(1, i)) + [i] + list(range(i - 1, 0, -1))
        line_str = ' '.join(str(n) for n in numbers)
        spaces = (rows - i) * 2
        result.append(' ' * spaces + line_str)
    return result

if __name__ == '__main__':
    pyramid = build_symmetric_pyramid(6)
    for line in pyramid:
        print(line)