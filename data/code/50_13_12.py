def inverted_right_angled_triangle(size):
    lines = []
    for i in range(size, 0, -1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = inverted_right_angled_triangle(5)
    print(result)