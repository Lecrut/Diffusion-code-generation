def inverted_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = '*' * i
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = inverted_triangle(5)
    print(result)