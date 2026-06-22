def inverted_right_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(inverted_right_triangle(5))