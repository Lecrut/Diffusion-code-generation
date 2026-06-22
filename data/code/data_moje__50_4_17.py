def hollow_triangle(n=8):
    lines = []
    for i in range(n):
        if i == 0:
            line = '*'
        elif i == n - 1:
            line = '*' * n
        else:
            line = '*' + ' ' * (i - 1) + '*'
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(hollow_triangle())